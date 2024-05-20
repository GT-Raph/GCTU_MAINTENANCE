from django.shortcuts import render
from django.http import HttpResponse
from .forms import MaintenanceRequestForm

# Create your views here.
def index(request):
    return render(request, 'MAINTENANCE/index.html')

def all_maintenance(request):
    return render(request, 'MAINTENANCE/all_maintenance.html')

def solved(request):
    return render(request, 'MAINTENANCE/solved.html')

def unsolved(request):
    return render(request, 'MAINTENANCE/unsolved.html')

def pending(request):
    return render(request, 'MAINTENANCE/pending.html')

def insoluble(request):
    return render(request, "MAINTENANCE/insoluble.html")

def workers(request):
    return render(request, 'MAINTENANCE/workers.html')

def request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MAINTENANCE/request_success')  # replace 'success_url' with the URL you want to redirect to after a successful form submission
    else:
        form = MaintenanceRequestForm()
    return render(request, 'MAINTENANCE/request.html', {'form': form})