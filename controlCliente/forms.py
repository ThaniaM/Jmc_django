#forms
from django import forms
from django.forms import ModelForm
from .models import Cliente,Servicio


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["id_cliente","nombre",  "correo","direccion", "telefono", "rfc","cp","estado","username","password","id_servicio"]
#el formulario va dependiendo los campops del modelo y los formularios usados en los modales
        #nota: respetar el orden para que funcione
    id_servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), empty_label=None)