from rest_framework import generics
from event.models import Event,Registration
from .serializers import EventSerializer,EventDetailSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

