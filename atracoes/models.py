from django.db import models

class Atracao(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.TextField()
	horario_fun_inicio = models.DateField()
	horario_fun_fim = models.DateField()
	idade_minima = models.IntegerField()
	foto = models.ImageField(upload_to="atracoes", null=True, blank=True)

	def __str__(self) -> str:
		return self.nome
