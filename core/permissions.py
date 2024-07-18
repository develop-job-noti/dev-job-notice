# System
from rest_framework.permissions import BasePermission

# Project


class HasSecureToken(BasePermission):
    def has_permission(self, request, view):
        # 요청이 인증되었는지 여부를 체크
        return getattr(request, "auth", None) is not None
