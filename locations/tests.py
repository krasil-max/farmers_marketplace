from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Location

User = get_user_model()

class LocationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.location = Location.objects.create(
            name='Nairobi',
            description='Capital of Kenya',
            latitude=-1.2921,
            longitude=36.8219
        )
        self.list_url = reverse('location-list')  # from DefaultRouter
        self.detail_url = reverse('location-detail', args=[self.location.id])

    def test_list_locations(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_location(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_location_requires_authentication(self):
        data = {
            'name': 'Kisumu',
            'description': 'City by Lake Victoria',
            'latitude': -0.0917,
            'longitude': 34.7679
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_location_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Mombasa',
            'description': 'Coastal city',
            'latitude': -4.0435,
            'longitude': 39.6682
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_location_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Nairobi Updated',
            'description': 'Updated Description',
            'latitude': -1.3,
            'longitude': 36.8
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_location_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

