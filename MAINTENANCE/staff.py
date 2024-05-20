from django.db import models
from django.contrib.auth import get_user_model

class MaintenanceStaff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='maintenance_staff')
    name = models.CharField(max_length=255, null=True, blank=True, default=None)
    # Add other fields as needed

    def __str__(self):
        return self.user.username