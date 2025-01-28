from django.db import models

from api.account.models import User
from core.models import AbstractBaseModel


class ToDo(AbstractBaseModel):
    title = models.CharField(max_length=255, unique=True, help_text="El título debe ser único.")
    description = models.TextField(blank=True, help_text="Descripción opcional de la tarea.")
    is_completed = models.BooleanField(default=False, help_text="Estado de la tarea, completada o no.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación de la tarea.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha de última actualización de la tarea.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_dos",
                             help_text="El usuario dueño de la tarea.")

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'user')  # Cada usuario puede tener títulos únicos
        ordering = ['-created_at']  # Ordenar resultados por fecha de creación
