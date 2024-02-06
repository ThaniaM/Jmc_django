#urls
from django.urls import path
from django.contrib.auth.decorators import login_required #que sea necesario iniciar sesion
from .views import handle_ajax_error

from . import views
urlpatterns = [
    path('create',views.create_cliente, name='create'),
    path('listar', login_required (views.listar_cliente), name='listar'),
    path('editar_cliente/<int:id_cliente>', login_required (views.update_cliente), name='editar_cliente'),
    path('eliminar/<int:id_cliente>', views.delete_cliente, name='eliminar_cliente'),
    path('handle_ajax_error/', handle_ajax_error, name='handle_ajax_error'),

] 






















    #path('create_clientes',views.create_clientes, name='create_clientes'),
    #path('save', login_required(views.save_clientes), name='save'),
    #path('save', views.save_clientes, name='save'),
    #path('control', login_required(views.listar_clientes), name='control'),
   # path('', views.listar_clientes, name='controlClientes'),
   # path('editar', views.update_clientes, name='editar_clientes'),
    #path('editar/<int:id_cliente>', login_required(views.update_clientes), name='editar_clientes'),
    #path('eliminar/<int:id_cliente>', views.delete_clientes, name='eliminar_clientes'),