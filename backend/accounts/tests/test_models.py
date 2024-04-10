from django.test import TestCase
from accounts.models import CustomUser


class CustomUserTestCase(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            email = 'test@gmail.com',
            username = 'test',
            password = 'test1234'
        )
        CustomUser.objects.create_superuser(
            email = 'admintest@gmail.com',
            username = 'admintest',
            password = 'admintest1234'
        )

    def test_email(self):
        normal_user = CustomUser.objects.get(email='test@gmail.com')
        admin_user = CustomUser.objects.get(email='admintest@gmail.com')
        self.assertEqual(normal_user.email, 'test@gmail.com')
        self.assertEqual(admin_user.email, 'admintest@gmail.com')
    
    def test_username(self):
        normal_user = CustomUser.objects.get(email='test@gmail.com')
        admin_user = CustomUser.objects.get(email='admintest@gmail.com')

        self.assertEqual(normal_user.username, 'test')
        self.assertEqual(admin_user.username, 'admintest')

    def test_password(self):
        normal_user = CustomUser.objects.get(email='test@gmail.com')
        admin_user = CustomUser.objects.get(email='admintest@gmail.com')

        self.assertTrue(normal_user.check_password('test1234'))
        self.assertTrue(admin_user.check_password('admintest1234'))
        
    def test_to_verify_if_adminuser_foi_setado_como_issuperuser_istaff(self):
        admin_user = CustomUser.objects.get(email="admintest@gmail.com")
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
