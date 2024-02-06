from django.urls import path

#vistas
from . import views

#configurar url
urlpatterns = [
  path('', views.menuAspel, name='menuAspel'),
  path('sae/', views.sae, name='sae'),
  path('coi/', views.coi, name='coi'),
  path('noi /', views.noi , name='noi'),
  path('caja/', views.caja, name='caja'),
  path('adm/', views.adm, name='adm'),
  path('facture/', views.facture, name='facture'),
  path('prod/', views.prod, name='prod'),
  path('banco/', views.banco, name='banco'),
]