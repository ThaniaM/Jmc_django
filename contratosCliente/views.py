# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from control_Contratos.models import Contrato

@login_required
def mostrar_contratos(request):
    cliente_actual = request.user

    # Lógica para obtener contratos asociados a cliente_actual
    contratos = Contrato.objects.filter(id_cliente=cliente_actual)

    return render(request, 'contratos-cliente.html', {'contratos': contratos})
