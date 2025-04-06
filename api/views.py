from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from products.views import ProductViewSet, CategoryViewSet
from reviews.models import ProductReview
from reviews.serializers import ProductReviewSerializer

# A simple read-only viewset for users; this can be limited to admin use if needed.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Aggregated Review ViewSet for full CRUD on reviews.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
