"""from django.urls import path
from . import views
app_name = "core"

urlpatterns = [
    path("", views.index, name= "index")
]"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_monoambiente/', views.crear_monoambiente, name='crear_monoambiente'),
    path('crear_un_dormitorio/', views.crear_un_dormitorio, name='crear_un_dormitorio'),
    path('crear_dos_dormitorios/', views.crear_dos_dormitorios, name='crear_dos_dormitorios'),
   
]
