from django.shortcuts import render

# Create your views here.
def empresa(request):
    return render(request, 'empresa.html')