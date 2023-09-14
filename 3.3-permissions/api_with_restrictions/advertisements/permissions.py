from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f'user is: {request.user.username}')
        print(f'user is: {request.user.username == "admin"}')
        if request.method == 'GET' or request.user.username == 'admin' or request.user.username == 'admin2':
            return True
        return request.user == obj.creator

