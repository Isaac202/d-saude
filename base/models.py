from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe



class Empresa(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    cpf = models.CharField(max_length=20, blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True, unique=True)
    area_empresa = models.CharField(max_length=10, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    dominio = models.CharField(max_length=255, unique=True, blank=True, null=True)



class Endereco(models.Model):
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=500, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)

class Usuarios(User):
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    status_user = models.CharField(max_length=100, blank=True)
    endereco_id = models.ForeignKey('Endereco', on_delete=models.CASCADE, blank=True, null=True)
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    tipo_user = models.CharField(max_length=50, blank=True, null=True)
    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.imagem.url}">'

class Servico(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    

class Horario(models.Model):
    dia_1 = models.CharField(max_length=255, blank=True, null=True)
    dia_2 = models.CharField(max_length=255, blank=True, null=True)
    dia_3 = models.CharField(max_length=255, blank=True, null=True)
    dia_4 = models.CharField(max_length=255, blank=True, null=True)
    dia_5 = models.CharField(max_length=255, blank=True, null=True)
    dia_6 = models.CharField(max_length=255, blank=True, null=True)
    dia_7 = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    
    
class Orden(models.Model):
    servico = models.ForeignKey('Servico', on_delete=models.CASCADE, blank=True, null=True)
    criado_por = models.CharField(max_length=10, blank=True, null=True)
    proficional = models.CharField(max_length=255, blank=True,null=True)
    email_proficional = models.CharField(max_length=255, blank=True,null=True)
    status = models.CharField( max_length=20, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True,null=True)
    paciente = models.CharField(max_length=255, blank=True,null=True)
    email_pacitente = models.CharField(max_length=255, blank=True,null=True)
    
    
    



