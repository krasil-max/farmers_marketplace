from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser, FarmerProfile
from products.models import Product, Category

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user and farmer profile
        self.user = CustomUser.objects.create_user(username='farmer1', password='testpass123', is_farmer=True)
        self.farmer_profile = FarmerProfile.objects.create(user=self.user)


        # Authenticate the client
        self.client.force_authenticate(user=self.user)

        # Create a category
        self.category = Category.objects.create(name="Vegetables", description="Fresh farm produce")

        # Create a product
        self.product = Product.objects.create(
            farmer=self.farmer_profile,
            title='Tomatoes',
            description='Fresh red tomatoes',
            price=120.00,
            category=self.category,
            inventory_count=50
        )

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tomatoes')

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            "title": "Cabbage",
            "description": "Organic cabbage",
            "price": 60.00,
            "category_id": self.category.id,
            "inventory_count": 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Cabbage')
