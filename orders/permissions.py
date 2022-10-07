from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.customer == request.user:
            return True

        # if request.user.is_staff and request.method not in self.edit_methods:
        #     return True

        return False
