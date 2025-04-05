from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, FarmerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_image', 'is_farmer', 'is_admin']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create user using the create_user method which handles password hashing.
        user = CustomUser.objects.create_user(**validated_data)
        return user

class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields = ['id', 'user', 'name', 'location', 'phone_number', 'whatsapp_link', 'profile_image', 'average_rating']
        read_only_fields = ['user', 'average_rating']
