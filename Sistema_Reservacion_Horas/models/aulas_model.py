from django.db import models

class Estado(models.Model):
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.descripcion


class Campus(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class Edificios(models.Model):
    descripcion = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class TiposAulas(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class AulasLaboratorios(models.Model):
    descripcion = models.CharField(max_length=255)
    tipo_aula = models.ForeignKey(TiposAulas, on_delete=models.CASCADE)
    edificio = models.ForeignKey(Edificios, on_delete=models.CASCADE)
    capacidad = models.IntegerField()
    cupos_reservados = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class TiposUsuarios(models.Model):
    identificador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class Usuario(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, unique=True)
    no_carnet = models.CharField(max_length=20, unique=True)
    tipo_usuario = models.ForeignKey(TiposUsuarios, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tanda(models.Model):
    descripcion = models.CharField(max_length=80)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, unique=True)
    tanda = models.ForeignKey(Tanda, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


