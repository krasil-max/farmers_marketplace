from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import FarmerProfile
from products.models import Category

User = get_user_model()

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='farmer', password='password')
        self.user.is_farmer = True
        self.user.save()

        self.farmer_profile = FarmerProfile.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name='Vegetables', description='Test category')

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'title': 'Test Product',
            'description': 'A test product',
            'price': 100.00,
            'category_id': self.category.id,
            'inventory_count': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
