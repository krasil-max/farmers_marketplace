# api/views.py

from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserSerializer  # Updated import name
from products.views import ProductViewSet, CategoryViewSet
from reviews.models import ProductReview
from reviews.serializers import ProductReviewSerializer

# Aggregated viewset for users (read-only)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Aggregated viewset for reviews
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
