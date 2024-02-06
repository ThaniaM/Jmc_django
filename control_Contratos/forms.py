from django import forms
from .models import Contrato
from controlCliente.models import Servicio,Cliente

class ContratoForm(forms.ModelForm):

    id_servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), empty_label=None)
    id_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label=None)

    class Meta:
        model = Contrato
        fields =  '__all__'
       


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Asegúrate de que los campos de llaves foráneas estén correctamente vinculados a los objetos de la base de datos
        self.fields['id_cliente'].queryset = Cliente.objects.all()
        self.fields['id_servicio'].queryset = Servicio.objects.all()

   

    