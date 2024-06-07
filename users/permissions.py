from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    """Пермишен на собственника объекта"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser


class IsUserUser(BasePermission):
    """Пермишен на редактирование своего профиля"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsUserTrader(BasePermission):
    """Пермишен на продавца и суперпользователя"""

    def has_permission(self, request, view):
        return request.user.is_trader or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_trader or request.user.is_superuser
