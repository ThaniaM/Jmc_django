from django.contrib import messages
from django.shortcuts import render
from .models import Contrato
from .forms import ContratoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from controlCliente .models import Cliente

def create_Contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        
        if form.is_valid():
            contrato_instance = form.save(commit=False)
            
            # Asignar las llaves foráneas desde el formulario
            contrato_instance.id_servicio = form.cleaned_data['id_servicio']
                
            contrato_instance.save()
            

            messages.success(request, 'Datos insertados correctamente.')
            return redirect('listar_contrato')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)
    else:
        form = ContratoForm()

    return render(request, 'control-contratos.html', {'form': form})
def listar_Contrato(request):
    contratos = Contrato.objects.all()
    
    return render(request, 'control-contratos.html', {'contratos': contratos})

def update_Contrato(request, id_contrato):
    contrato = get_object_or_404(Contrato, id_contrato=id_contrato)
    
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            contrato_instance = form.save(commit=False)

            contrato_instance.id_cliente = form.cleaned_data['id_cliente']
            contrato_instance.save()

            # Incluye el ID de la categoría en la respuesta
            data = {
                'message': 'Datos actualizados correctamente',
                'id_servicio': contrato_instance.id_servicio_id,
                'id_cliente': contrato_instance.id_cliente_id,
            }
            return redirect('listar_contrato')

        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'fecha_contrato': contrato.fecha_contrato,
            'vigencia_contrato': contrato.vigencia_contrato,
            'id_servicio': contrato.id_servicio_id,
            'id_cliente': contrato.id_cliente_id,

        }

        return JsonResponse(data)

@csrf_exempt    
def delete_Contrato(request, id_contrato):
    # Obtiene la instancia del producto
    contrato = get_object_or_404(Contrato, id_contrato=id_contrato)

    # Elimina el producto
    contrato.delete()

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