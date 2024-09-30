from django.db import models

class Campus(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Edificios(models.Model):
    descripcion = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class TiposAulas(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class AulasLaboratorios(models.Model):
    descripcion = models.CharField(max_length=255)
    tipo_aula = models.ForeignKey(TiposAulas, on_delete=models.CASCADE)
    edificio = models.ForeignKey(Edificios, on_delete=models.CASCADE)
    capacidad = models.IntegerField()
    cupos_reservados = models.IntegerField()
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, unique=True)
    no_carnet = models.CharField(max_length=20, unique=True)
    tipo_usuario = models.ForeignKey('TiposUsuarios', on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

class TiposUsuarios(models.Model):
    identificador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion
