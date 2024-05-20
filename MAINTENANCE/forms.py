from django import forms
from .models import MaintenanceRequest, CustomUser

class MaintenanceRequestForm(forms.ModelForm):
    check_repaired_by = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = MaintenanceRequest
        fields = '__all__'