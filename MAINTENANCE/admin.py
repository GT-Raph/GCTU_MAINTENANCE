from django.contrib import admin
from .models import MaintenanceRequest

class MaintenanceRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('department_location', 'person_making_request', 'contact', 'category_of_request', 'description_of_request')
        }),
        ('Editable Fields', {
            'fields': ('check_repaired_by', 'date_of_completion', 'approval_by_property', 'process')
        }),
    )
    readonly_fields = ('department_location', 'person_making_request', 'contact', 'category_of_request', 'description_of_request')

admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)