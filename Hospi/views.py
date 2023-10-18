from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Medico,Paciente, Medicamentos
 
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
    fields = "__all__"
    template_name = 'Medico_actualizar.html'
    success_url = reverse_lazy('Medico_listado') 

class MedicoEliminar(SuccessMessageMixin, DeleteView): 
    model = Medico 
    fields = "__all__" 
    template_name = 'Medico_eliminar.html'
    success_url = reverse_lazy('Medico_listado') 

# Vistas para el modelo Paciente
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = "__all__"
    template_name = 'paciente_create.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = "__all__"
    template_name = 'paciente_update.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_delete.html'
    success_url = reverse_lazy('paciente_list')

# Vistas para el modelo Medicamentos
class MedicamentosListView(ListView):
    model = Medicamentos
    template_name = 'medicamentos_list.html'

class MedicamentosDetailView(DetailView):
    model = Medicamentos
    template_name = 'medicamentos_detail.html'

class MedicamentosCreateView(CreateView):
    model = Medicamentos
    fields = "__all__"
    template_name = 'medicamentos_create.html'
    success_url = reverse_lazy('medicamentos_list')

class MedicamentosUpdateView(UpdateView):
    model = Medicamentos
    fields = "__all__"
    template_name = 'medicamentos_update.html'
    success_url = reverse_lazy('medicamentos_list')

class MedicamentosDeleteView(DeleteView):
    model = Medicamentos
    template_name = 'medicamentos_delete.html'
    success_url = reverse_lazy('medicamentos_list')