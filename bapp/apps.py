from django.apps import AppConfig

class BappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bapp'
def ready(self):
    import bapp.signals