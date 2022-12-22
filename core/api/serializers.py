from rest_framework.serializers import ModelSerializer
from core.models import PontosTuristico

class PontoTuristicoSerializer(ModelSerializer):
	class Meta:
		model = PontosTuristico
		fields = ('id', 'nome', 'descricao')