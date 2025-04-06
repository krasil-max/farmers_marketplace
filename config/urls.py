"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# api/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users.views import UserViewSet
from products.views import ProductViewSet, CategoryViewSet
from locations.views import CountyViewSet, SubCountyViewSet, WardViewSet
from reviews.views import ReviewViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'counties', CountyViewSet, basename='county')
router.register(r'subcounties', SubCountyViewSet, basename='subcounty')
router.register(r'wards', WardViewSet, basename='ward')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]


