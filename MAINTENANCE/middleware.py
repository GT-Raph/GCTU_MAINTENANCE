# middleware.py

from django.contrib.auth import logout
from django.conf import settings
from django.utils import timezone

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if 'last_activity' is set in the session
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Calculate the time elapsed since last activity
                elapsed_time = timezone.now() - last_activity
                if elapsed_time.total_seconds() > settings.SESSION_COOKIE_AGE:
                    # Logout the user if the session has expired
                    logout(request)
            # Update 'last_activity' in the session
            request.session['last_activity'] = timezone.now()

        response = self.get_response(request)
        return response
