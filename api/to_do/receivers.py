from django.db.models.signals import post_save
from django.dispatch import receiver

from api.to_do.models import ToDo
from api.to_do.tasks import send_task_completed_notification


@receiver(post_save, sender=ToDo)
def trigger_notification_on_completion(sender, instance, created, **kwargs):
    if not created and instance.is_completed:
        # Llamar a la tarea de Celery
        send_task_completed_notification.delay(instance.id)

