from django.shortcuts import render

# Create your views here.
def menuAspel(request):
  return render(request, 'menuAspel.html')

def coi(request):
  return render(request, 'coi.html')

def sae(request):
  return render(request, 'sae.html')

def noi(request):
  return render(request, 'noi.html')

def banco(request):
  return render(request, 'banco.html')

def caja(request):
  return render(request, 'caja.html')

def facture(request):
  return render(request, 'facture.html')

def adm(request):
  return render(request, 'adm.html')

def prod(request):
  return render(request, 'prod.html')
