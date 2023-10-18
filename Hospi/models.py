from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100, default='') 
    especialidad = models.CharField(max_length=20, default='')  
    edad = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Paciente(models.Model):
    nombre = models.CharField(max_length=100, default='') 
    cedula = models.CharField(max_length=20, default='')  
    edad = models.CharField(max_length=20, default='')
    direccion =  models.CharField(max_length=200, default='')
    antecedentes = models.CharField(max_length=100, default='')
    diagnostico = models.CharField(max_length=100, default='')
    medicacion = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   

class Medicamentos(models.Model):
    medicamento = models.CharField(max_length=100, default='') 
    unidades = models.CharField(max_length=20, default='')  
    miligramos = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

class Meta:
    db_table = 'medicos'
    db_table = 'pacientes'
    db_table = 'medicamentos'