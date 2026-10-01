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



#  python manage.py  makemigrations 
#  python manage.py  migrate 
    