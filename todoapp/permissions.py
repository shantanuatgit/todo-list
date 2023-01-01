from rest_framework import permissions

OBJECT_SAFE_METHODS = ()

class IsOwnerOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj ):
        admin_permission = bool(request.user and request.user.is_staff)
        if request.method in OBJECT_SAFE_METHODS:
            return True
        return obj.task_user == request.user or admin_permission

class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)