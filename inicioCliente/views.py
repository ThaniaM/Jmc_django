from django.shortcuts import render

# Create your views here.
def inicioCliente(request):
    return render(request, 'inicio-cliente.html')