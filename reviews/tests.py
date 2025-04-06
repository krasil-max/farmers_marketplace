from users.models import CustomUser, FarmerProfile
from products.models import Product, Category
from rest_framework.test import APITestCase

class ReviewAPITests(APITestCase):

    def setUp(self):
        # Create a test user and farmer profile
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')
        self.farmer_profile = FarmerProfile.objects.create(user=self.user, name='Test Farmer', location='Test Location')
        
        # Create a test category
        self.category = Category.objects.create(name='Test Category', description='A category for testing')
        
        # Create a test product
        self.product = Product.objects.create(
            farmer=self.farmer_profile,
            title='Test Product',  # Use the 'title' field instead of 'name'
            description='A product for testing',
            price=10.99,
            category=self.category,
            inventory_count=100
        )
        
        # Create a test review (assuming ProductReview model exists)
        self.review = ProductReview.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment='Great product!'
        )
        
        # Log in the user
        self.client.login(username='testuser', password='password123')
