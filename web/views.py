from rest_framework.settings import perform_import
from .models import PenulisanIlmiah
from .serializers import PenulisanSerializer
from rest_framework import viewsets, permissions

class PenulisanViewset(viewsets.ModelViewSet):
    queryset = PenulisanIlmiah.objects.all()
    serializer_class = PenulisanSerializer
    permission_classes = [permissions.IsAuthenticated]