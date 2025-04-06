from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, FarmerProfileSerializer

# Registration view
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# Custom login view using token authentication
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Login with POST only."})

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
        })


# Profile view for the logged in user
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Farmer Profile view (if you want to update farmer-specific data)
class FarmerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure that the farmer profile exists; otherwise, you might create one here.
        profile, created = CustomUser.objects.get(id=self.request.user.id).farmer_profile.get_or_create(
            user=self.request.user,
            defaults={'name': self.request.user.username}
        )
        return profile
