from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100, default='') 
    especialidad = models.CharField(max_length=20, default='')  
    edad = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Luchador(models.Model):
    nombreLuchador = models.CharField(max_length=100, default='')
    ArteMarcialLuchador= models.CharField(max_length=20,default='')
    edadLuchador = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'medicos'
    db_table = 'Luchadores'