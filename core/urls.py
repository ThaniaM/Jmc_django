from django.urls import path

#vistas
from . import views

#configurar url
urlpatterns = [
  path('', views.index, name='index'),
]

