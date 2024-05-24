from django.contrib import admin
from .models import MaintenanceRequest
from django.utils.html import format_html
from django.contrib.auth.models import Group


admin.site.site_header = 'GCTU PHYSICAL DEVELOPMENT'



class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('department_location', 'person_making_request', 'category_of_request', 'display_checked_by', 'process', 'is_completed')
    
    def display_checked_by(self, obj):
        checked_by_users = [str(user) for user in obj.check_repaired_by.all()]
        if checked_by_users:
            return ", ".join(checked_by_users)
        else:
            return "Not assigned"
    display_checked_by.short_description = 'Checked By'
    
    def is_completed(self, obj):
        return obj.date_of_completion is not None
    is_completed.short_description = 'Completed'
    is_completed.boolean = True
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields
        return ()
    
    fieldsets = (
        (None, {
            'fields': ('department_location', 'person_making_request', 'contact', 'category_of_request', 'description_of_request')
        }),
        ('Editable Fields', {
            'fields': ('check_repaired_by', 'date_of_completion', 'approval_by_property', 'process', 'status')
        }),
    )
    readonly_fields = ('department_location', 'person_making_request', 'contact', 'category_of_request', 'description_of_request')

admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)
admin.site.unregister(Group)