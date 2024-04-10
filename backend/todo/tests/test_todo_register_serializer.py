from django.test import TestCase
from todo.serializers import TodoRegisterSerializer
from accounts.models import CustomUser
from todo.models import ToDo

class TodoRegisterSerializerTestCase(TestCase):

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
            "title":"title test",
            "description":"description test",
            "status": "pending",
            "priority":"low",
        }
        serializer = TodoRegisterSerializer(data=valid_data)

        self.assertTrue(serializer.is_valid(raise_exception=True))

        saved_instance = serializer.save()
        self.assertIsInstance(saved_instance, ToDo)