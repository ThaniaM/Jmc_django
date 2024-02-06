from django.shortcuts import render #funciones de djang
from .models import Servicio #importa el modelo de servicio de la app
from controlCliente.models import Cliente
from control_Contratos.models import Contrato

def uno(request):
     # Obtener la categoría con id_categoria=1
    servicio = Servicio.objects.get(id_servicio=1)

    # Obtener las subcategorías asociadas a la categoría
    clientes = Cliente.objects.filter(id_servicio=servicio)
    # Obtener todos los productos relacionados con las subcategorías
    contratos = Contrato.objects.filter(id_cliente__in=clientes)
    
    return render(request, 'control-ajuste.html', {'servicio': servicio, 'clientes': clientes, 'contratos': contratos})

def dos(request):
     # Obtener la categoría con id_categoria=1
    servicio = Servicio.objects.get(id_servicio=2)

    # Obtener las subcategorías asociadas a la categoría
    clientes = Cliente.objects.filter(id_servicio=servicio)

    return render(request, 'control-ajuste.html', {'servicio': servicio, 'clientes': clientes})
def tres(request):
    # Obtener la categoría con id_categoria=1
    servicio = Servicio.objects.get(id_servicio=3)

    # Obtener las subcategorías asociadas a la categoría
    clientes = Cliente.objects.filter(id_servicio=servicio)
    return render(request, 'control-ajuste.html', {'servicio': servicio, 'clientes': clientes})
def cuatro(request):
    # Obtener la categoría con id_categoria=1
    servicio = Servicio.objects.get(id_servicio=4)

    # Obtener las subcategorías asociadas a la categoría
    clientes = Cliente.objects.filter(id_servicio=servicio)
    return render(request, 'control-ajuste.html', {'servicio': servicio, 'clientes': clientes})
def cinco(request):
    # Obtener la categoría con id_categoria=1
    servicio = Servicio.objects.get(id_servicio=5)

    # Obtener las subcategorías asociadas a la categoría
    clientes = Cliente.objects.filter(id_servicio=servicio)
    return render(request, 'control-ajuste.html', {'servicio': servicio, 'clientes': clientes})
