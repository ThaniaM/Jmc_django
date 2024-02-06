from django.shortcuts import render

# Create your views here.
def inicioAdmin(request):
    return render(request, 'inicio-Admin.html')