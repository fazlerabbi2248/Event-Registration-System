from rest_framework import serializers
from event.models import Event,Registration
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location','slots_available']


# Details of a specific event

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['username'] # need only user name for retrive details for a specific event

    def get_username(self, obj):
        return obj.user.username


class EventDetailSerializer(serializers.ModelSerializer):
    registered_users = RegistrationSerializer(many=True, source='registration_set')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location','slots_available', 'registered_users']


class UserLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password']