from django.urls import path, include

from event import views

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')), # this is build in
    path('register/', views.register, name='register'), # custom
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create_event'),


]