from django import forms
from django.forms import ModelForm
from .models import Staff
from django.core.validators import RegexValidator


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["id_staff","nombre", "departamento","telefono", "username", "password"]
    #RegexValidator, que es una clase proporcionada por Django para validar campos de texto utilizando expresiones regulares.
    telefono_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Ingrese un número de teléfono válido (puede incluir el código de país)."
    )
    nombre_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El nombre debe contener solo letras y espacios."
    )
    username_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s]+$',
        message="Este campo solo puede contener letras y números."
    )
    password_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s]+$',
        message="El password debe contener solo letras y números."
    )
    #Se le está aplicando la validación
    telefono = forms.CharField(validators=[telefono_validator])
    nombre = forms.CharField(validators=[nombre_validator])
    username = forms.CharField(validators=[username_validator])
    password = forms.CharField(validators=[password_validator])
#los métodos clean_<campo> son utilizados para realizar validaciones personalizadas para un campo específico.
def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
def clean_username(self):
        username = self.cleaned_data.get('username')
def clean_passsword(self):
        password= self.cleaned_data.get('password')