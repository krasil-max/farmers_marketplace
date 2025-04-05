from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoryViewSet
from users.views import FarmerViewSet
from reviews.views import ReviewCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'reviews', ReviewCreateView)

urlpatterns = [
    path('', include(router.urls)),  # Aggregated API routes
]
