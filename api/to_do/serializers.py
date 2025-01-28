from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        # Obtener el usuario actual del contexto de la solicitud
        user = self.context['request'].user

        # Verificar si ya existe un ToDo con el mismo título y usuario, excluyendo el actual
        to_do_instance = self.instance  # Esto obtiene el objeto actual, si está en modo de actualización
        if ToDo.objects.filter(title=value, user=user).exclude(
                uuid=to_do_instance.uuid if to_do_instance else None).exists():
            raise serializers.ValidationError("Ya existe una tarea con este título para el usuario actual.")
        return value

    def validate(self, data):
        # Validación adicional si es necesario (por ejemplo, reglas personalizadas)
        if len(data.get('title', '')) < 3:  # Verificar longitud mínima del título
            raise serializers.ValidationError({'title': "El título debe tener al menos 3 caracteres."})
        return data

    class Meta:
        model = ToDo
        fields = ['uuid', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']
