from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_maintenance/', views.all_maintenance, name='all_maintenance'),
    path('solved/', views.solved, name='solved'),
    path('unsolved/', views.unsolved, name='unsolved'),
    path('pending/', views.pending, name='pending'),
    path('insoluble/', views.insoluble, name='insoluble'),
    path('workers/', views.workers, name='workers'),
    path('request/', views.request, name='request'),
]
