from typing import Any

from django.http import Http404
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsOwnerOfObject(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        if obj.user != request.user:
            raise Http404  # 404 to prevent object revelation
        return True
