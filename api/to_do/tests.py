from rest_framework.test import APITestCase
from rest_framework import status
from api.to_do.models import ToDo
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken  # Importar para generar el token
from faker import Faker

User = get_user_model()
fake = Faker()


class BaseAPITestCase(APITestCase):
    def authenticate_user(self, user):
        """Autentica al usuario y agrega el token Bearer en los headers"""
        token = str(AccessToken.for_user(user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')


class ToDoCreateTestCase(BaseAPITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
        )

    def test_create_to_do(self):
        self.authenticate_user(self.user)  # Autenticar usuario

        # Datos para crear una tarea
        data = {
            "title": "Nueva tarea",
            "description": "Esta es una nueva tarea"
        }

        # Realizar la solicitud POST al endpoint
        response = self.client.post('/v1/todos/', data)

        # Asegurarse de que la respuesta sea exitosa
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])


class ToDoListTestCase(BaseAPITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
        )
        self.todo1 = ToDo.objects.create(user=self.user, title="Tarea 1", description="Primera tarea")
        self.todo2 = ToDo.objects.create(user=self.user, title="Tarea 2", description="Segunda tarea")

    def test_list_to_dos_auth_user(self):
        self.authenticate_user(self.user)  # Autenticar usuario

        # Solicitar la lista de tareas
        response = self.client.get('/v1/todos/')

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_to_dos_unauth_user(self):
        # Usuario sin autenticarse
        response = self.client.get('/v1/todos/')

        # Verificar que la respuesta sea un error 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ToDoRetrieveTestCase(BaseAPITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.user2 = User.objects.create_user(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.todo_user1 = ToDo.objects.create(user=self.user1, title="Tarea de user1", description="Tarea para user1")
        self.todo_user2 = ToDo.objects.create(user=self.user2, title="Tarea de user2", description="Tarea para user2")

    def test_retrieve_to_do_own_task(self):
        self.authenticate_user(self.user1)  # Autenticar como user1

        response = self.client.get(f'/v1/todos/{self.todo_user1.uuid}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Tarea de user1")

    def test_retrieve_to_do_other_task(self):
        self.authenticate_user(self.user1)  # Autenticar como user1

        response = self.client.get(f'/v1/todos/{self.todo_user2.uuid}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ToDoUpdateTestCase(BaseAPITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.todo = ToDo.objects.create(user=self.user, title="Tarea inicial", description="Descripción inicial")

    def test_update_to_do(self):
        self.authenticate_user(self.user)  # Autenticar usuario

        data = {
            "title": "Tarea actualizada",
            "description": "Descripción actualizada",
            "is_completed": True
        }
        response = self.client.put(f'/v1/todos/{self.todo.uuid}/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['is_completed'], True)


class ToDoDeleteTestCase(BaseAPITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.todo = ToDo.objects.create(user=self.user, title="Tarea para eliminar", description="Será eliminada")

    def test_delete_to_do(self):
        self.authenticate_user(self.user)  # Autenticar usuario

        response = self.client.delete(f'/v1/todos/{self.todo.uuid}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_to_do_unauth_user(self):
        response = self.client.delete(f'/v1/todos/{self.todo.uuid}/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
