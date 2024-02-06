import base64
from django.contrib import messages
from django.shortcuts import render
from .models import Pago
from .forms import PagoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from controlCliente .models import Cliente
from django.core.files.base import ContentFile

def create_Pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        
        if form.is_valid():
            pago_instance = form.save(commit=False)
            
            
            # Asignar las llaves foráneas desde el formulario
            pago_instance.id_servicio = form.cleaned_data['id_servicio'] 
            pago_instance.save()
            

            messages.success(request, 'Datos insertados correctamente.')
            return redirect('listar_pago')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)
    else:
        form = PagoForm()

    return render(request, 'control-pagos.html', {'form': form})

def listar_Pago(request):
    pagos = Pago.objects.all()

    for pago in pagos:
        if pago.pdf:
            pago.pdf = base64.b64decode(pago.pdf.encode())

    return render(request, 'control-pagos.html', {'pagos': pagos})

def update_Pago(request, id_pago):
    pago = get_object_or_404(Pago, id_pago=id_pago)
    if request.method == 'POST':
        form = PagoForm(request.POST, request.FILES, instance=pago)
        if form.is_valid():
            pago_instance = form.save(commit=False)

            # Convertir el archivo PDF a hexadecimal
            if request.FILES.get('pdf'):
                pdf_file = request.FILES['pdf']
                pago_instance.pdf.save(pdf_file.name, ContentFile(pdf_file.read()))

            pago_instance.id_cliente = form.cleaned_data['id_cliente']
            pago_instance.save()

            # Incluye el ID de la categoría en la respuesta
            data = {
                'message': 'Datos actualizados correctamente',
                'id_servicio': pago_instance.id_servicio_id,
                'id_cliente': pago_instance.id_cliente_id,
            }
            return redirect('listar_pago')

        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    

@csrf_exempt    
def delete_Pago(request, id_pago):
    # Obtiene la instancia del producto
    pago = get_object_or_404(Pago, id_pago=id_pago)

    # Elimina el producto
    pago.delete()

    return JsonResponse({'message': 'Registro eliminado correctamente'})

def obtener_clientes(request):
    try:
        id_servicio = request.GET.get('id_servicio')
        
        if id_servicio is not None:
            clientes = Cliente.objects.filter(id_servicio_id=id_servicio)
            data = [{'id': sub.id_cliente, 'nombre': sub.nombre} for sub in clientes]
            # Cambiado el nombre del campo de 'id_subcategoria_id' a 'id_subcategoria'
        else:
            data = []

        return JsonResponse(data, safe=False)
    except Exception as e:
        print('Error:', str(e))
        return JsonResponse({'error': str(e)}, status=500)
    