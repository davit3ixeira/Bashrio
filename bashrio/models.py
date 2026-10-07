from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefone = models.CharField(max_length=14, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    @property
    def nome(self):
        if self.user.first_name:
            return self.user.first_name
        return self.user.username
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def cpf_formatado(self):
        """Retorna o CPF formatado como XXX.XXX.XXX-XX"""
        if not self.cpf:
            return None
        cpf = self.cpf.replace('.', '').replace('-', '').replace(' ', '')
        if len(cpf) == 11:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return self.cpf

class Organizador(models.Model):
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    local = models.CharField(max_length=200, blank=True, null=True)
    preco = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    duracao = models.TimeField(blank=True, null=True)
    informacoes = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.titulo