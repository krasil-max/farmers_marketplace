from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Admin').exists()

class IsFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Farmer').exists()

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Buyer').exists()
