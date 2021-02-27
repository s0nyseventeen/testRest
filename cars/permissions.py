from rest_framework import persmissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    check if user is owner of post, we can change data
    '''
    def has_object_permission(self, request, view, obj):
        if request.me in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user