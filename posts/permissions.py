# 커스텀화하는 PERMISSIONS
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissions를 커스텀화하고 오직 owner만 수정할 수 있도록
    """
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user