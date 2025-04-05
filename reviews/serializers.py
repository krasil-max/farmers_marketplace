# reviews/serializers.py
from rest_framework import serializers
from .models import ProductReview
from products.models import Product
from users.models import CustomUser

class ProductReviewSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ProductReview
        fields = ['product', 'product_title', 'user', 'user_username', 'rating', 'comment', 'created_at']

    def validate(self, attrs):
        # Ensure a user cannot review the same product more than once
        user = self.context['request'].user
        product = attrs.get('product')

        if ProductReview.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("You have already reviewed this product.")
        return attrs
