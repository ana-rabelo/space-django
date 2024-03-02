from django.utils import timezone
from django.db import models

class Fotografia(models.Model):

    OPC_CAT = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
        ("OUTRO", "Outro")
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPC_CAT, default="Outro")
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return f"Fotografia: [{self.nome}]"