from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=256)
    email = models.EmailField()
    nacimiento = models.DateField()



class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=256)
    email = models.EmailField()
    nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    entrega = models.DateTimeField()
    aprobado = models.BooleanField(default = False)







