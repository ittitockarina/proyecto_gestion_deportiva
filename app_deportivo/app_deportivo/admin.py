from django.contrib import admin
from .models import (Deporte, Entrenador, Federacion, Equipo, Atleta, Instalacion,
                     Disciplina, Categoria, Competencia, Medalla, Resultado, 
                     Inscripcion, Usuario, Evento, Sponsor, EventoSponsor, 
                     ParticipacionAtleta, Entrenamiento)

admin.site.register(Deporte)
admin.site.register(Entrenador)
admin.site.register(Federacion)
admin.site.register(Equipo)
admin.site.register(Atleta)
admin.site.register(Instalacion)
admin.site.register(Disciplina)
admin.site.register(Categoria)
admin.site.register(Competencia)
admin.site.register(Medalla)
admin.site.register(Resultado)
admin.site.register(Inscripcion)
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Sponsor)
admin.site.register(EventoSponsor)
admin.site.register(ParticipacionAtleta)
admin.site.register(Entrenamiento)
