from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Medico
 
from django.urls import reverse
 
from django.contrib import messages
  
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms


class MedicoListado(ListView):
    model = Medico  

class MedicoCrear(SuccessMessageMixin, CreateView):
    model = Medico 
    form = Medico 
    fields = "__all__" 
    success_message = 'Medico Creada Correctamente!' 
        
    
    def get_success_url(self):
        return reverse('leer')

class MedicoDetalle(DetailView): 
    model = Medico  


class MedicoActualizar(SuccessMessageMixin, UpdateView): 
    model = Medico  
    form = Medico 
    fields = "__all__"  
    success_message = 'Medico Actualizada Correctamente !'
    
    
    def get_success_url(self):               
        return reverse('leer') 

class MedicoEliminar(SuccessMessageMixin, DeleteView): 
    model = Medico 
    form = Medico
    fields = "__all__"     
    
        
    def get_success_url(self): 
        success_message = 'Medico Eliminada Correctamente !'  
        messages.success (self.request, (success_message))       
        return reverse('leer') 