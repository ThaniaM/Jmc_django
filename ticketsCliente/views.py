from django.shortcuts import render

# Create your views here.
def ticketsCliente(request):
    return render(request, 'tickets-cliente.html')