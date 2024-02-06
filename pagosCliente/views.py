# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from control_Pagos.models import Pago

@login_required
def mostrar_pagos(request):
    cliente_actual = request.user

    # Lógica para obtener pagos asociados a cliente_actual
    pagos = Pago.objects.filter(id_cliente=cliente_actual)

    return render(request, 'pagos-cliente.html', {'pagos': pagos})
