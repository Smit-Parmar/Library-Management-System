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

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        print(request.user!="AnonymousUser")
        if request.method in SAFE_METHODS:
            print(request.user!="AnonymousUser")
            return True
        elif request.user!="AnonymousUser":
            return True