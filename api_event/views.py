from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from event.models import Event,Registration
from .serializers import EventSerializer,EventDetailSerializer,UserLoginSerializer,EventRegistrationSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserLoginView(APIView):
  permission_classes = []

  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['username or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class EventRegistrationView(generics.CreateAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        user = self.request.user

        event = Event.objects.get(id=event_id)

        queryset = Registration.objects.filter(user=user, event_id=event_id).exists()

        if queryset:
            return Response({'error': 'You are already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if event.slots_available > 0:

                serializer = self.get_serializer(data={'user': self.request.user.id, 'event': event_id})

                serializer.is_valid(raise_exception=True)
                serializer.save(user=user, event_id=event_id)
                event.slots_available -= 1
                event.save()
                return Response({'success': 'Successfully registered for the event.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'No available slots for this event.'}, status=status.HTTP_400_BAD_REQUEST)


