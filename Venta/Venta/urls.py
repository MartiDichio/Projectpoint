"""
URL configuration for Venta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("fotos/", include("fotos.urls")),

]
from django.urls import path
from . import views
app_name = "ventas"

urlpatterns = [
    path("", views.index, name= "index")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_monoambiente/', views.crear_monoambiente, name='crear_monoambiente'),
    path('crear_un_dormitorio/', views.crear_un_dormitorio, name='crear_un_dormitorio'),
    path('crear_dos_dormitorios/', views.crear_dos_dormitorios, name='crear_dos_dormitorios'),
   
]