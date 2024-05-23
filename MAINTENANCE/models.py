from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission

CATEGORY = (
    ('Carpentry', 'Carpentry'),
    ('Electrical', 'Electrical'),
    ('Air-condition', 'Air-condition'),
    ('Plumbing', 'Plumbing'),
    ('Other', 'Other'),
)

PROCESS_CHOICES = (
    ('pending', 'Pending'),
    ('solved', 'Solved'),
    ('unsolved', 'Unsolved'),
    ('insoluble', 'Insoluble'),
)

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

class MaintenanceRequest(models.Model):
    date_of_request = models.DateField(auto_now_add=True)
    department_location = models.CharField(max_length=100)
    person_making_request = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    category_of_request = models.CharField(max_length=100, choices=CATEGORY)
    description_of_request = models.TextField()
    check_repaired_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='checked_requests')
    date_of_completion = models.DateField(null=True, blank=True)
    approval_by_property = models.BooleanField(default=False)
    process = models.CharField(max_length=10, choices=PROCESS_CHOICES, default='pending')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.status == 'completed' and not self.date_of_completion:
            self.date_of_completion = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Maintenance Request #{self.pk}"
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Override the groups and user_permissions fields
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')