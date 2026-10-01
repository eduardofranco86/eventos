from django.forms import ModelForm
from .models import Evento

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