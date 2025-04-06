from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, FarmerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_image', 'is_farmer', 'is_admin']

class RegisterSerializer(serializers.ModelSerializer):
    is_farmer = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_farmer']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields = ['id', 'user', 'name', 'location', 'phone_number', 'whatsapp_link', 'profile_image', 'average_rating']
        read_only_fields = ['user', 'average_rating']
