from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Category
from users.models import CustomUser, FarmerProfile

class ReviewAPITests(APITestCase):
    def setUp(self):
        # Setup code, create necessary objects
        self.category = Category.objects.create(name='Test Category')
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.farmer_profile = FarmerProfile.objects.create(user=self.user)
        self.product = Product.objects.create(
            farmer=self.farmer_profile,
            title='Test Product',
            description='Test product description',
            price=10.00,
            category=self.category
        )
    
    def test_create_review(self):
        # Your test code here
        response = self.client.post('/api/reviews/', data={'product': self.product.id, 'rating': 5, 'comment': 'Great product!'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reviews(self):
        # Your test code here
        response = self.client.get(f'/api/products/{self.product.id}/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
