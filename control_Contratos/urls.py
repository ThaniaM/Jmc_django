# urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns =[
    path('create_contrato',views.create_Contrato, name='create_contrato'),
    path('listar_contrato', login_required (views.listar_Contrato), name='listar_contrato'),
    path('editar_contrato/<int:id_contrato>', login_required (views.update_Contrato), name='editar_contrato'),
    path('eliminar/<int:id_contrato>', views.delete_Contrato, name='eliminar_contrato'),
    path('obtener_clientes/', views.obtener_clientes, name='obtener_clientes'),
    
]