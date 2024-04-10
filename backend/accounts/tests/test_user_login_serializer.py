from django.test import TestCase
from accounts.serializers import UserLoginSerializer
from accounts.models import CustomUser



class LoginSerializerTestCase(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            email="test@gmail.com",
            username="test",
            password="test1234"
        )

    def test_to_virify_login_serilizer_loggedin_successfully(self):
        data_to_test = {
            "email": "test@gmail.com",
            "password": "test1234"
        }
        serializer = UserLoginSerializer(data=data_to_test)

        self.assertTrue(serializer.is_valid())

        user = serializer.check_user(data=data_to_test)

        self.assertIsInstance(user, CustomUser)