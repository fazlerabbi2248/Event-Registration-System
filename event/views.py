from datetime import datetime, date

from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from event.models import Event,Registration
from .forms import CustomUserCreationForm, EventForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def home(request):
    query = request.GET.get('query')
    if query:
        all_events = Event.objects.filter(
            Q(title__icontains=query) | Q(location__icontains=query)
        )
    else:
        all_events = Event.objects.all()

    context = {
        'all_events': all_events,
    }

    return render(request,'home.html',context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def upcoming_events(request):
    current_datetime = timezone.now()
    upcoming_events = Event.objects.filter(date__gt=current_datetime).order_by('date')

    context = {
        'upcoming_events': upcoming_events,
        'current_datetime': current_datetime
    }
    return render(request, 'upcoming_events.html', context)

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user


    if Registration.objects.filter(event=event, user=user).exists():
        messages.warning(request, 'You are already registered for this event.')
        return redirect('upcoming_events')
    else:
        registration = Registration(event=event, user=user)
        registration.save()
        event.slots_available -= 1
        event.save()
        messages.success(request, 'You have successfully registered for the event.')
    return redirect('registered_events')





@login_required
def user_registered_events(request):
    user = request.user
    today = timezone.now().date()


    registered_events = Registration.objects.filter(
        user=user,
        event__date__gte=today
    ).select_related('event')

    username = user.get_username()

    context = {
        'username': username,
        'registered_events': registered_events,
    }
    return render(request, 'registered_events.html', context)


@login_required
def unregister_event(request, event_id):
    user = request.user
    event = get_object_or_404(Event, pk=event_id)

    registration = Registration.objects.filter(event=event, user=user).first()
    if registration:
        registration.delete()
        event.slots_available += 1
        event.save()
        messages.success(request, 'You have successfully unregistered from the event.')
    else:
        messages.warning(request, 'You are not registered for this event.')

    return redirect('registered_events')

@login_required
def participate_events(request):
    user = request.user
    today = timezone.now().date()

    participate_events = Registration.objects.filter(user=user,event__date__lt=today).select_related('event')

    username = user.get_username()

    context = {
        'username': username,
        'participate_events': participate_events,
    }
    return render(request, 'participate_events.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')