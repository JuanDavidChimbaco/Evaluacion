from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    programas_registrados = models.ManyToManyField('Programa')
    
    def __str__(self):
        return self.nombre

class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    ficha = models.IntegerField()
    codigo = models.IntegerField()
    cupo = models.IntegerField()
    duracionMeses = models.IntegerField()
    jornada = models.CharField(max_length=6)

    def __str__(self):
        return self.nombre