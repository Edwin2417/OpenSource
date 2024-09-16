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
