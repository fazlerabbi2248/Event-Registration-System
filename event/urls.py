from django.urls import path, include

from event import views

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')), # this is build in
    path('register/', views.register, name='register'), # custom
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/upcoming/', views.upcoming_events, name='upcoming_events'),
    path('event/register/<int:event_id>/', views.register_event, name='register_event'),
    path('event/register/participate_events/', views.participate_events, name='participate_events'),
    path('event/register/registered_events/', views.user_registered_events, name='registered_events'),
    path('event/unregister/<int:event_id>/', views.unregister_event, name='unregister_event'),
    path('logout/', views.logout_view, name='logout'),


]