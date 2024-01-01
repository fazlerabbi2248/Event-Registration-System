from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from event.models import Event

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'slots_available']