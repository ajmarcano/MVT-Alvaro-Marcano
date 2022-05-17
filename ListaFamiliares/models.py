from django.db import models

class familiaLopez(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    años = models.IntegerField(0)