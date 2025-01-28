from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListCreateView(ListCreateAPIView):
    """
    Endpoint para listar y crear tareas del usuario autenticado.
    """
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtener tareas solo del usuario autenticado
        return ToDo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asignar usuario autenticado al crear una tarea
        serializer.save(user=self.request.user)


class ToDoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Endpoint para ver, actualizar o eliminar una tarea específica.
    """
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtener tareas solo del usuario autenticado
        return ToDo.objects.filter(user=self.request.user)
