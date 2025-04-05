from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ProductReview
from .serializers import ProductReviewSerializer
from rest_framework.exceptions import ValidationError

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        if ProductReview.objects.filter(user=self.request.user, product=product).exists():
            raise ValidationError("You have already reviewed this product.")
        serializer.save(user=self.request.user)
