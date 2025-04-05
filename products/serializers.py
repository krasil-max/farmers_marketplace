from rest_framework import serializers
from .models import Product, Category
from users.models import FarmerProfile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    farmer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price',
            'category', 'category_id', 'image',
            'inventory_count', 'average_rating',
            'farmer', 'created_at'
        ]
        read_only_fields = ['id', 'farmer', 'average_rating', 'created_at']
