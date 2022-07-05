from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow creator of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         print(request.user)
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the creator of the movie
#         return obj.creator == request.user

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