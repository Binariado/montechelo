from django.apps import AppConfig


class ToDoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.to_do'

    def ready(self):
        import api.to_do.receivers
