from django.db import models
from departamentos.models import *
# Create your models here.
class Empleado(models.Model):
    codigo = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    


    def __str__(self): # self representa el objeto
        # return self.nombre
        return f'{self.nombre} ° {self.codigo_departamento} '