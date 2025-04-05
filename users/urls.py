from django.urls import path
from .views import RegisterView, CustomAuthToken, UserProfileView, FarmerProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('farmer-profile/', FarmerProfileView.as_view(), name='farmer_profile'),
]
