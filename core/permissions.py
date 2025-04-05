from rest_framework import permissions

class IsFarmerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow farmers to edit their products.
    All users can view the products.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow all users to read (GET, HEAD, OPTIONS)

        return request.user.is_authenticated and request.user.is_farmer  # Only farmers can edit
