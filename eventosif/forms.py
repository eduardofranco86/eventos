from django.forms import ModelForm
from .models import Contato, Evento

# Publicadores de cursos 

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = [
            "titulo",
            "descricao",
            "data_inicio",
            "data_fim",
            "local",
            "categoria",
            "informacoes_adicionais",
        ]


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = [
            "nome",
            "email",
            "mensagem",
        ]