#urls
from django.urls import path
from django.contrib.auth.decorators import login_required #que sea necesario iniciar sesion

from . import views
urlpatterns = [
    path('create_staff',views.create_staff, name='create_staff'),
    path('listar_staff', login_required (views.listar_staff), name='listar_staff'),
    path('editar_staff/<int:id_staff>', login_required (views.update_staff), name='editar_staff'),
    path('eliminar/<int:id_staff>', views.delete_staff, name='eliminar_staff'),
] 






