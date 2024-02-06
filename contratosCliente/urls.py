# urls.py
from django.urls import path
from .views import mostrar_contratos

urlpatterns = [
    path('contratos/', mostrar_contratos, name='mostrar_contratos'),
    # Otras URL de tu aplicación
]
