from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):

    message = "you can't edit or delete this snack object , you are not a superUser !!"
    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser
    
    def has_permission(self, request, view):
        if request.method == "GET": return True
        return request.user.is_superuser