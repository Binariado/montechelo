from django.urls import path, include
from rest_framework import routers

from api.to_do.views import ToDoListCreateView, ToDoRetrieveUpdateDestroyView

router = routers.DefaultRouter()

urlpatterns = [
    path('todos/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<uuid:pk>/', ToDoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
    path('', include(router.urls)),
]
