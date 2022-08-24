from rest_framework import permissions

#Admin Permissions for List Create API view
class AdminCreatePermission(permissions.DjangoModelPermissions):
    def has_permission(self,request, view):
        if request.method == 'POST' and not request.user.is_staff:
                return False
        return True
#User Persmission for Purchasing and listing Orders
class NormalUserPermission(permissions.DjangoModelPermissions):
    def has_permission(self,request, view):
        if request.user.is_staff:
                return False
        return True