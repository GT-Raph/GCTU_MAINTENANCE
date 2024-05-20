from django import forms
from crispy_forms.helper import FormHelper
from .models import MaintenanceRequest, CustomUser

class MaintenanceRequestForm(forms.ModelForm):
    check_repaired_by = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = MaintenanceRequest
        fields = '__all__'
        


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['department_location', 'person_making_request', 'contact', 'category_of_request', 'description_of_request']
        widgets = {
            'department_location': forms.TextInput(attrs={'placeholder': 'Department location'}),
            'person_making_request': forms.TextInput(attrs={'placeholder': 'Person making request'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Contact'}),
            'category_of_request': forms.Select(),  # Assuming category_of_request is a ForeignKey or ChoiceField
            'description_of_request': forms.Textarea(attrs={'placeholder': 'Description of request'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # customize the helper if needed