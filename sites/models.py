from django.db import models
from base.models import Empresa

class SiteConf(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    cor_1 = models.CharField(max_length=20, blank=True, null=True)
    cor_2 = models.CharField(max_length=20, blank=True, null=True)
    cor_3 = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TimeField(blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
