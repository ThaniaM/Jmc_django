from django.urls import path

#vistas
from . import views

#configurar url
#despues del views. es el nombre que se pone en la funcion en el archivo vistas
urlpatterns = [
  path('', views.empresa, name='empresa'),
]