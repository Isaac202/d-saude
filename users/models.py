from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from base.models import Endereco, Empresa

# Create your models here.

class Usuarios(User):
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    status_user = models.CharField(max_length=100, blank=True)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, blank=True, null=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.imagem.url}">'
    
