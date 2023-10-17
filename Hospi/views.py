from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Medico
 
from django.urls import reverse_lazy
 
from django.contrib import messages
  
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

class HomeView(ListView):
    model = Medico
    template_name = 'index.html'

class MedicoListado(ListView):
    model = Medico
    template_name = 'Medico_listado.html'

class MedicoCrear(SuccessMessageMixin, CreateView):
    model = Medico 
    fields = "__all__" 
    template_name = 'Medico_crear.html'
    success_url = reverse_lazy('Medico_listado')
 
class MedicoDetalle(DetailView): 
    model = Medico  


class MedicoActualizar(SuccessMessageMixin, UpdateView): 
    model = Medico  
    form = Medico 
    fields = "__all__"
    template_name = 'Medico_actualizar.html'
    success_url = reverse_lazy('Medico_actualizar') 

class MedicoEliminar(SuccessMessageMixin, DeleteView): 
    model = Medico 
    form = Medico
    fields = "__all__" 
    template_name = 'Medico_eliminar.html'
    success_url = reverse_lazy('Medico_eliminar') 