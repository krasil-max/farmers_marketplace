from rest_framework import viewsets, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from core.permissions import IsFarmerOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsFarmerOrReadOnly]

    def perform_create(self, serializer):
        # Ensure only authenticated farmers can create
        serializer.save(farmer=self.request.user.farmer_profile)

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_farmer:
            return Product.objects.filter(farmer=self.request.user.farmer_profile)
        return Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can manage categories
