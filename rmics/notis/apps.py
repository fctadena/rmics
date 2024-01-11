from django.apps import AppConfig


class NotisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notis'
    def ready(self): 
        try: 
            import notis.signals 
        except ImportError: 
            pass
