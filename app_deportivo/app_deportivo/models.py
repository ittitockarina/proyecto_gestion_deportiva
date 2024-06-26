from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    rol = models.CharField(
        max_length=50, 
        choices=[
            ('atleta', 'Atleta'), 
            ('entrenador', 'Entrenador'), 
            ('administrador', 'Administrador')
        ]
    )

    def __str__(self):
        return self.user.username


class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #falta usuario 
class Federacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    




class Atleta(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    faltas = models.TextField(blank=True, null=True)  # tarjeta amarilla, roja
   

class Instalacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    encargado = models.CharField(max_length=100)
    

class Disciplina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()

class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

#cambialo por premio
class Medalla(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=20)
    #
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

class Resultado(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    posicion = models.IntegerField()
    tiempo = models.TimeField()
    puntos = models.IntegerField()

class Inscripcion(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #precio





class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    federacion = models.ForeignKey(Federacion, on_delete=models.CASCADE)

class Sponsor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)

class EventoSponsor(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

class ParticipacionAtleta(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100, blank=True, null=True)

class Entrenamiento(models.Model):
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
