from django.apps import AppConfig


class MaintenanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MAINTENANCE'
    
    def ready(self):
        import MAINTENANCE.signals  # replace 'yourapp' with the name of your app
