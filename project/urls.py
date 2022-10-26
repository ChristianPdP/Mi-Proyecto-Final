"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (imc, index, monstrar_familiares, mostrar_mi_template, saludar_a, saludo,
                            BuscarFamiliar, AltaFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
#from blog.views import index as blog_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('saludar_a/<nombre>', saludar_a),   
    path('saludar-desde-el-primer-template/', index),
    path('mostrar-mi-template/', mostrar_mi_template),
    path('imc/', imc),
    path('mi-familia/', monstrar_familiares),
 #   path('blog/', blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),  
    path('panel-familia/', FamiliarList.as_view(), name="familiar-list"), 
    path('panel-familia/crear', FamiliarCrear.as_view(), name="familiar-crear"), 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"),   
]