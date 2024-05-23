from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import MaintenanceRequestForm
from .models import MaintenanceRequest 
from google.cloud import recaptchaenterprise_v1
from google.cloud.recaptchaenterprise_v1 import Assessment

def create_assessment(project_id: str, recaptcha_key: str, token: str, recaptcha_action: str) -> Assessment:
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()
    event = recaptchaenterprise_v1.Event()
    event.site_key = recaptcha_key
    event.token = token

    assessment = recaptchaenterprise_v1.Assessment()
    assessment.event = event

    project_name = f"projects/{project_id}"

    request = recaptchaenterprise_v1.CreateAssessmentRequest()
    request.assessment = assessment
    request.parent = project_name

    response = client.create_assessment(request)

    if not response.token_properties.valid:
        print("The CreateAssessment call failed because the token was invalid for the following reasons: ", response.token_properties.invalid_reason)
        return

    if response.token_properties.action != recaptcha_action:
        print("The action attribute in your reCAPTCHA tag does not match the action you are expecting to score")
        return

    for reason in response.risk_analysis.reasons:
        print(reason)
    print("The reCAPTCHA score for this token is: ", response.risk_analysis.score)
    assessment_name = client.parse_assessment_path(response.name).get("assessment")
    print(f"Assessment name: {assessment_name}")
    return response

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'MAINTENANCE/login.html')

@login_required
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
    unsolved_maintenance = MaintenanceRequest.objects.filter(process='unsolved', check_repaired_by=request.user)
    return render(request, 'MAINTENANCE/unsolved.html', {'maintenance': unsolved_maintenance})

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

@login_required
def workers(request):
    workers = User.objects.exclude(id=request.user.id)
    workers_with_requests = [{'worker': worker, 'requests': MaintenanceRequest.objects.filter(check_repaired_by=worker)} for worker in workers]
    return render(request, 'MAINTENANCE/workers.html', {'workers_with_requests': workers_with_requests})

def request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_success')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'MAINTENANCE/request.html', {'form': form})

def request_success(request):
    return render(request, 'MAINTENANCE/request_success.html')