"""
URL configuration for ProyectoLAB3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  Hospi.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , HomeView.as_view(), name = 'index'),

    path('Hospi/' , HomeView.as_view(), name = 'index'), 
    
    path('Medico/Listado', MedicoListado.as_view(), name='Medico_listado'),

    path('Medico/detalle/<int:pk>', MedicoDetalle.as_view(), name='Medico_detalles'),
     
    path('Medico/', MedicoCrear.as_view(), name='Medico_crear'),

    path('Medico/editar/', MedicoActualizar.as_view(), name='Medico_actualizar'), 

    path('Medico/eliminar/', MedicoEliminar.as_view(), name='Medico_eliminar'),   

    ]
    
