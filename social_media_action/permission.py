from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Permission that allows editing/deleting an object only for the owner.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        if isinstance(obj, request.user.__class__):
            return obj == request.user

        return getattr(obj, "user", None) == request.user
