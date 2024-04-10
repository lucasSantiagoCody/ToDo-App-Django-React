from django.test import TestCase
from accounts.models import CustomUser
from accounts.serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    
    valid_data = {
        "email": "test@gmail.com",
        "username": "test",
        "password": "test1234"
    }


    def test_valid_data(self):

        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertTrue(user.check_password("test1234"))

    def test_invalid_data(self):

        invalid_data = {
            'email': 'invalidgmail.com',
            'username': 'invalid',
            'password': ''
        }

        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        

    def test_register_user(self):

        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, CustomUser)
