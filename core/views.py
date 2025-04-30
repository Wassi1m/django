from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdmin, IsManager, IsReservationManager
from rest_framework.permissions import IsAuthenticated

class EtageViewSet(ModelViewSet):
    # ... existing code ...
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin|IsManager]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ChambreViewSet(ModelViewSet):
    # ... existing code ...
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin|IsManager]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ReservationViewSet(ModelViewSet):
    # ... existing code ...
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAdmin|IsReservationManager]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes] 