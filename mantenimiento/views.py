from django.shortcuts import render

# Create your views here.
def mantenimiento(request):
    return render(request, 'mantenimiento.html')