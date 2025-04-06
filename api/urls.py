from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ReviewViewSet
from products.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
