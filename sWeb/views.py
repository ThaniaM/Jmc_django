from django.shortcuts import render

# Create your views here.
def sWeb(request):
    return render(request, 'sWeb.html')