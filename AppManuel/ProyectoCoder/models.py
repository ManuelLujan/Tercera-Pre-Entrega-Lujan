from django.db import models

# Create your models here.


class Monotributo(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cuit=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.cuit}"

class Profesion(models.Model):
    actividad=models.CharField(max_length=50)
    moneda=models.CharField(max_length=50)
    ingresos_brutos=models.IntegerField()

class Vencimientos(models.Model):
    cuit=models.IntegerField()
    fecha_vencimiento=models.DateField()
    pagaDeServicio=models.BooleanField()