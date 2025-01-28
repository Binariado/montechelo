from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
from api.to_do.models import ToDo
import logging

logger = logging.getLogger(__name__)

#
# @shared_task
# def send_task_completed_notification(todo_id):
#     try:
#         # Obtén la tarea de la base de datos
#         todo = ToDo.objects.get(id=todo_id)
#
#         # Información para enviar la notificación (puede ser correo o log)
#         subject = f"Tarea completada: {todo.title}"
#         message = f"¡Hola {todo.user.username}!\n\nTu tarea '{todo.title}' ha sido marcada como completada.\n\nGracias por usar nuestro servicio."
#         recipient_list = [todo.user.email]
#
#         # Enviar correo
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
#         return f"Notificación enviada correctamente para la tarea: {todo.title}"
#     except ToDo.DoesNotExist:
#         return f"Tarea con ID {todo_id} no encontrada."
#


@shared_task
def send_task_completed_notification(todo_id):
    try:
        todo = ToDo.objects.get(id=todo_id)
        logger.info(f"Notificación: Tarea '{todo.title}' completada por el usuario {todo.user.username}.")
    except ToDo.DoesNotExist:
        logger.error(f"No se encontró la tarea con ID: {todo_id}.")

