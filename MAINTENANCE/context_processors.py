# In a new file, e.g. context_processors.py
from django.contrib.auth.models import User
from .models import MaintenanceRequest

def nav_view_number(request):
    insoluble_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='insoluble')
    all_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user)
    pending_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='pending')
    solved_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='solved')
    unsolved_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='unsolved')
    workers_assigned = User.objects.filter(checked_requests__in=all_requests).distinct().count()
    return {
        'all_count': all_requests.count(),
        'pending_count': pending_requests.count(),
        'solved_count': solved_requests.count(),
        'unsolved_count': unsolved_requests.count(),
        'insoluble_count': insoluble_requests.count(),
        'workers_count': workers_assigned,
    }