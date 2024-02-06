from django.urls import path
from django.contrib.auth.decorators import login_required #que sea necesario iniciar sesion
#vistas
from . import views

#configurar url
#despues del views. es el nombre que se pone en la funcion en el archivo vistas
urlpatterns = [
    path('create_equipo',views.create_equipo, name='create_equipo'),
    path('listar_equipo', login_required (views.listar_equipo), name='listar_equipo'),
    path('editar_equipo/<int:id_equipo>', login_required (views.update_equipo), name='editar_equipo'),
    path('eliminar/<int:id_equipo>', views.delete_equipo, name='eliminar_equipo'),
    path('obtener_clientes/', views.obtener_clientes, name='obtener_clientes'),
]