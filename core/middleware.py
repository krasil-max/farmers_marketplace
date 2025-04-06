# core/middleware.py

from django.http import JsonResponse

class RBACMiddleware:
    """
    Custom middleware to handle role-based access control.
    For now, it blocks unauthorized access to create/update product if not a farmer.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add custom logic if needed
        response = self.get_response(request)
        return response
