from django.urls import path, include

from event import views

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')), # this is build in
    path('register/', views.register, name='register'), # custom
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/upcoming/', views.upcoming_events, name='upcoming_events'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('register/registered_events', views.user_registered_events, name='registered_events'),


]