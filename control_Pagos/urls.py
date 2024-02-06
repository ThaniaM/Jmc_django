# urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns =[
    path('create_pago',views.create_Pago, name='create_pago'),
    path('listar_pago', login_required (views.listar_Pago), name='listar_pago'),
    path('editar_pago/<int:id_pago>', login_required (views.update_Pago), name='editar_pago'),
    path('eliminar/<int:id_pago>', views.delete_Pago, name='eliminar_pago'),
    path('obtener_clientes/', views.obtener_clientes, name='obtener_clientes'),
    
]