from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListAPIView.as_view(), name='event-list-api'),
    path('events/<int:pk>/', views.EventDetailAPIView.as_view(), name='event-detail-api'),
    path('login/', views.UserLoginView.as_view(), name='login-api'),
    path('event/<int:event_id>/register/', views.EventRegistrationView.as_view(), name='event-registration'),
    path('event/registeredevents/', views.RegisteredEventListAPIView.as_view(), name='event-Registered'),
]