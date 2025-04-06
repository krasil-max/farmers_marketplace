from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class CustomAuthTokenTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'secret123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login_url = reverse('login')

    def test_login_successful(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
