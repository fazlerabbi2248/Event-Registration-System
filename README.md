# Event Registration System

## Description
This is an Event Registration System developed using Django and Django Rest Framework, allowing users to register, login, create events, register for events, and view event details.

## Features
- **User Registration and Authentication**: Users can create accounts and log into the system using Django's default User model.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/user_registration.png)
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/login.png)
  
- **Dashboard Access**: After logging in, users can access the dashboard.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/dashboard.png)
  
- **Event Creation**: Authenticated users can create new events.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/createevent.png)
  
- **Event Registration**: Users can register for upcoming events if slots are available, which decreases the available slots by 1.

  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/registerevent.png)
  
- **Event Unregistration**: Authenticated users can unregister from events they've registered for, increasing the available slots by 1.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/unregister.png)
  
- **Participated Events**: Users can view events they have participated in.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/participated.png)
  
- **Event Search**: Users can search for events or event locations.
  
  ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/search_event.png)
  
- **Logout**: Users can log out of the system.


## API Endpoints (Using Django Rest Framework)

1. `/api/events/` - List of all events.
   
   ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/all_events.png)
  
3. `/api/events/<event_id>/` - Details of a specific event.
   
   ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/details_event.png)
   
5. `/api/login/` - User login.
   
   ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/logapi.png)
   
7. `/api/event/event_id>/register/` - User registration for an event.
   
   ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/reg_Api.png)
   
9. `/api/event/registeredevents/` - User's registered events.
    
    ![Dashboard](https://github.com/fazlerabbi2248/Event-Registration-System/blob/master/all_reg_api.png)


