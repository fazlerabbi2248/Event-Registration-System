from rest_framework import generics
from event.models import Event,Registration
from .serializers import EventSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
