from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsManager(permissions.BasePermission):
    """Permission pour le manager qui gère les étages et chambres"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'

class IsReservationManager(permissions.BasePermission):
    """Permission pour le responsable des réservations"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'reservation' 