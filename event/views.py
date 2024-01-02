from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login as auth_login
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
    return render(request, 'home.html')

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
    else:
        registration = Registration(event=event, user=user)
        registration.save()
        messages.success(request, 'You have successfully registered for the event.')
    return redirect('home')


@login_required
def user_registered_events(request):
    user = request.user
    registered_events = Registration.objects.filter(user=user).select_related('event')
    username =user.get_username()

    context = {
        'username': username,
        'registered_events': registered_events,
    }
    return render(request, 'registered_events.html', context)