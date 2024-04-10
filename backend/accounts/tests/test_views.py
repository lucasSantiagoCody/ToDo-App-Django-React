from django.test import TestCase
from django.urls import reverse 
from accounts.models import CustomUser


class RegisterViewTestCase(TestCase):

    def test_register_view_valid_data(self):

        url = reverse('register-view')

        valid_data = {
            "email": "test@gmail.com",
            "username": "test",
            "password": "test1234"
        }

        response = self.client.post(url, valid_data, format='json')
        self.assertEqual(response.status_code, 201)
    
    def test_register_view_invalid_data(self):

        url = reverse('register-view')
        
        invalid_data = {
            "email": "test@.com",
            "username": "test",
            "password": "test",

        }

        response = self.client.post(url, invalid_data, format='json')
        self.assertTrue(response.status_code, 400)

class LoginViewTestCase(TestCase):
    
    def setUp(self):
        CustomUser.objects.create_user(
            email='test@gmail.com',
            username='test',
            password='test1234'
        ).save()

    def test_login_valid_data(self):
        url = reverse('login-view')
        valid_data = {
            "email": "test@gmail.com",
            "password": "test1234"
        }

        response = self.client.post(url, valid_data, format='json')

        self.assertEqual(response.status_code, 200)
    
    def test_login_invalid_data(self):
        url = reverse('login-view')

        invalid_data = {
            "email": "xxxxxx@gmail.com",
            "password": ""
        }

        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, 404)


class LogoutViewTestCase(TestCase):

    def test_logout(self):

        url = reverse('logout-view')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)