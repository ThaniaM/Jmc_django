# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from controlSoporte.models import Equipo

@login_required
def mostrar_equipos(request):
    cliente_actual = request.user

    # Lógica para obtener contratos asociados a cliente_actual
    equipos = Equipo.objects.filter(id_cliente=cliente_actual)

    return render(request, 'clientes.html', {'equipos': equipos})
