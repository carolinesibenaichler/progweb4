from django.db import models
from django.utils import timezone

class Twip(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.CharField(max_length=140)
    data_criacao = models.DateTimeField(default=timezone.now)
    #adicionar outros campos relevantes aqui

    def __str__(self):
        return self.texto
    
