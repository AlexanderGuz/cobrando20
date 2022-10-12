from django.db import models

# Create your models here.
class Departamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presopuesto = models.FloatField()


    def __str__(self): # self representa el objeto
        return f'{self.nombre}'