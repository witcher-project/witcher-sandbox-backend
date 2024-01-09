from django.http import Http404
from rest_framework import permissions


class IsOwnerOfObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user != request.user:
            raise Http404  # Change the status code to 404 to prevent object revelation
        return True
