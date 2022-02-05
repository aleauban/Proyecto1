"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto1.views import saludo, segunda_vista, dia_de_hoy, mi_nombre, dia_de_hoy1, dia_de_hoy2, anio_nacimiento


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('diadehoy/', dia_de_hoy),
    path('prueba4/<nombre>/', mi_nombre), 
    path('diadehoy1/', dia_de_hoy1),
    path('diadehoy2/', dia_de_hoy2),
    path('nacimiento/<edad>', anio_nacimiento),
    #la parte naranja puede ser cualquier texto (es lo que se pone en la URL) y se pone <> el parametro   
]
