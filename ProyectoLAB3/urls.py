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
from  Hospi.views import MedicoListado,MedicoDetalle,Medico,MedicoActualizar,MedicoCrear,MedicoEliminar



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('Hospital/', MedicoListado.as_view(template_name = "templates/index.html"), name='leer'),

    
    path('Medico/detalle/<int:pk>', MedicoDetalle.as_view(template_name = "templates/detalles.html"), name='detalles'),

     
    path('Medico/crear', MedicoCrear.as_view(template_name = "templates/crear.html"), name='crear'),

    
    path('Medico/editar/<int:pk>', MedicoActualizar.as_view(template_name = "templates/actualizar.html"), name='actualizar'), 

    
    path('Medico/eliminar/<int:pk>', MedicoEliminar.as_view(), name='eliminar'),   
]
