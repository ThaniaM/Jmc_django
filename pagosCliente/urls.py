# urls.py
from django.urls import path
from .views import mostrar_pagos

urlpatterns = [
    path('pagos/', mostrar_pagos, name='mostrar_pagos'),
    # Otras URL de tu aplicación
]
