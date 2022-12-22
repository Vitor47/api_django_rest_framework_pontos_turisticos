from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontosTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
