from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import MaintenanceRequestForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import MaintenanceRequest 



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # or wherever you want to redirect after login
        else:
            # Invalid login
            pass
    return render(request, 'MAINTENANCE/login.html')
def index(request):
    return render(request, 'MAINTENANCE/index.html')

@login_required
def all_maintenance(request):
    user_maintenance = MaintenanceRequest.objects.filter(check_repaired_by=request.user)
    return render(request, 'MAINTENANCE/all_maintenance.html', {'maintenance': user_maintenance})

@login_required
def solved(request):
    solved_requests = MaintenanceRequest.objects.filter(process='solved', check_repaired_by=request.user)
    return render(request, 'MAINTENANCE/solved.html', {'requests': solved_requests})

@login_required
def unsolved(request):
    return render(request, 'MAINTENANCE/unsolved.html')

@csrf_exempt
def update_process(request, task_id):
    task = MaintenanceRequest.objects.get(id=task_id)
    task.process = request.POST['process']
    task.save()
    return redirect('pending')

@login_required
def pending(request):
    pending = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='pending')
    return render(request, 'MAINTENANCE/pending.html', {'maintenance': pending})

@login_required
def insoluble(request):
    insoluble_requests = MaintenanceRequest.objects.filter(check_repaired_by=request.user, process='insoluble')
    return render(request, "MAINTENANCE/insoluble.html", {'requests': insoluble_requests})

def workers(request):
    return render(request, 'MAINTENANCE/workers.html')

def request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_success')  # replace 'success_url' with the URL you want to redirect to after a successful form submission
    else:
        form = MaintenanceRequestForm()
    return render(request, 'MAINTENANCE/request.html', {'form': form})

def request_success(request):
    return render(request, 'MAINTENANCE/request_success.html')