from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('index/', views.index, name='index'),
    path('all_maintenance/', views.all_maintenance, name='all_maintenance'),
    path('solved/', views.solved, name='solved'),
    path('unsolved/', views.unsolved, name='unsolved'),
    path('pending/', views.pending, name='pending'),
    path('insoluble/', views.insoluble, name='insoluble'),
    path('workers/', views.workers, name='workers'),
    path('request/', views.request, name='request'),
    path('request/request_success/', views.request_success, name='request_success'),
    path('update_process/<int:task_id>/', views.update_process, name='update_process'),
]
