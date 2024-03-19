from rest_framework.permissions import BasePermission

class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        user_level = request.user.level
        if (user_level == "client" or
            user_level == "functionary" or
            user_level == "admin"
        ) and (
            request.user.is_authenticated
        ):
            return True
        return False

class FunctionaryPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user, request.user.is_authenticated)

        if request.method == "GET":
            return True
        else:
            user_level = request.user.level
            if (user_level == "functionary" or 
                user_level == "admin"
            ) and (
                request.user.is_authenticated
            ):
                return True

            return False

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        user_level = request.user.level
        if user_level == "admin" and (
            request.user.is_authenticated
        ):
            return True
        return False

