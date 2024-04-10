from django.test import TestCase
from todo.models import ToDo
from todo.serializers import TodoSerializer
from accounts.models import CustomUser



class TodoSerializerTestCase(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            email='test@gmail.com',
            username='test',
            password='test1234'
        )

    def test_valid_data(self):
        user = CustomUser.objects.get(email='test@gmail.com')
        valid_data = {
            "user": user.id,
            "title": "title test",
            "description": "description test",
            "priority": "low",
            "status": "pending"
        }

        serializer = TodoSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid())

        saved_instance = serializer.save()

        self.assertIsInstance(saved_instance, ToDo)