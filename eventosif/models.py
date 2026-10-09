from django.db import models

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    informacoes_adicionais = models.TextField(blank=True, null=True)   

    def __str__(self):
        return self.titulo




from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relacionamento 1 para 1 com o User do Django
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='perfil'
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    

#  python manage.py  makemigrations 
#  python manage.py  migrate 
    