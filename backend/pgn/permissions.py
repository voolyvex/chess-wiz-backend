from rest_framework.permissions import BasePermission

class CustomDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Implement your custom permission logic here
        # Check if the user has permission to delete the object
        
        # For example, you can check if the user is the owner of the game
        return obj.created_by == request.user
