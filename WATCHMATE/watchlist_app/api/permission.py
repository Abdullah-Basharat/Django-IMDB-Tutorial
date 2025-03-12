from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.reviewer == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows only admin users to edit/delete.
    Other users can only read (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # SAFE_METHODS are: GET, HEAD, OPTIONS (read-only)
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow read-only access

        # Otherwise, check if the user is an admin
        return request.user and request.user.is_staff
