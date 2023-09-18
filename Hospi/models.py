from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE') 
    especialidad = models.CharField(max_length=20, default='DEFAULT VALUE')  
    edad = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
class Meta:
    db_table = 'medicos'
