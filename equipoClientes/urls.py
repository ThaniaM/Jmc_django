# urls.py
from django.urls import path
from .views import mostrar_equipos

urlpatterns = [
    path('equipos/', mostrar_equipos, name='mostrar_equipos'),
    # Otras URL de tu aplicación
]
