from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # if obj.admin:
        #     if obj.admin == request.user:
        #         return True
        
        return obj.user_type== request.user

# class HasAdminOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):

#         # hover over SAFE_METHODS to see which qualify
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         if obj.admin is None:
#             return True

#         return obj.admin== request.user