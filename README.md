# Event Registration System

## Description
This is an Event Registration System developed using Django and Django Rest Framework, allowing users to register, login, create events, register for events, and view event details.

## Features
- **User Registration and Authentication**: Users can create accounts and log into the system using Django's default User model.
- **Dashboard Access**: After logging in, users can access the dashboard.
- **Event Creation**: Authenticated users can create new events.
- **Event Registration**: Users can register for upcoming events if slots are available, which decreases the available slots by 1.
- **Event Unregistration**: Authenticated users can unregister from events they've registered for, increasing the available slots by 1.
- **Participated Events**: Users can view events they have participated in.
- **Event Search**: Users can search for events or event locations.
- **Logout**: Users can log out of the system.

## API Endpoints (Using Django Rest Framework)
1. `/api/events/` - List of all events.
2. `/api/events/<event_id>/` - Details of a specific event.
3. `/api/login/` - User login.
4. `/api/event/event_id>/register/` - User registration for an event.
5. `/api/event/registeredevents/` - User's registered events.


