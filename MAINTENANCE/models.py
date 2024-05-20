from django.db import models
from django.conf import settings

CATEGORY = (
    ('Carpentry', 'Carpentry'),
    ('Electrical', 'Electrical'),
    ('Air-condition', 'Air-condition'),
    ('Plumbing', 'Plumbing'),
    ('Other', 'Other'),
)

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
    solved = models.BooleanField(default=False)

    def __str__(self):
        return f"Maintenance Request #{self.pk}"