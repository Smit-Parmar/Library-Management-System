from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow read only to user and CRUD to Admin
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_anonymous:
            return False
        else:
            return True