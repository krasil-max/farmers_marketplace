from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from products.models import Product, Category
from reviews.models import ProductReview

User = get_user_model()

class AggregatedAPITests(APITestCase):
    def setUp(self):
        # Create and authenticate a test user.
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        # Optionally, create a category for products.
        self.category = Category.objects.create(
            name="Test Category", 
            description="A category for testing."
        )
        # Optionally, create a product.
        # Note: If your Product model requires a farmer profile and your user is not a farmer,
        # the product list might remain empty. Adjust as necessary.
        # self.product = Product.objects.create(
        #     farmer=self.user.farmer_profile,  # Ensure the test user has a farmer profile if needed
        #     title="Test Product",
        #     description="A product for testing.",
        #     price=99.99,
        #     category=self.category,
        #     inventory_count=10
        # )
        # Optionally, create a review.
        # self.review = ProductReview.objects.create(
        #     product=self.product,
        #     user=self.user,
        #     rating=5,
        #     comment="Excellent!"
        # )

    def test_users_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_list(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories_list(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reviews_list(self):
        url = reverse("review-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
