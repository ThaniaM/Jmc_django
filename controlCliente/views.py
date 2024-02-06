from django.shortcuts import render #funciones de django
from .models import Servicio,Cliente #importa el modelo de cliente de la app
from .forms import ClienteForm #traer el formulario de cliente de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
             # Obtener la contraseña del formulario
            password = form.cleaned_data.get('password')

            # Cifrar la contraseña
            hashed_password = make_password(password)

            # Crear una instancia del formulario con la contraseña cifrada
            form.instance.password = hashed_password
            form.save()
            messages.success(request, 'Cliente creado con éxito.')
            return redirect('listar')
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            messages.error(request, 'Error al crear el cliente: {}'.format(errors))
            return redirect('listar')
    else:
        form = ClienteForm()
    return render(request, 'control-clientes.html', {'form': form}) 


#funcion para mostrar la lista de los clientes
def listar_cliente(request): #hacemos la solicitud al servidor con la funcion request
    clientes = Cliente.objects.all() #mostramos los clientes almacenaso en la base de datos
    return render (request, "control-clientes.html", {"clientes":clientes}) #respuesta del servidor en la pagina control-clientes

#funcion para actualizar o modificar los datos del cliente
def update_cliente(request, id_cliente): #obtener los datos del cliente mediante el id
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ClienteForm(request.POST, instance=cliente) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar') #se regresa al la pagina donde estan los clientes
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre':cliente.nombre,
            'correo': cliente.correo,
            'direccion':cliente.direccion,
            'telefono': cliente.telefono,
            'rfc':cliente.rfc,
            'cp':cliente.cp,
            'estado': cliente.estado,
            'username': cliente.username,
            'password': cliente.password,
            'id_servicio': cliente.id_servicio.id_servicio,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_cliente(request, id_cliente):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente) 
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion
    
def handle_ajax_error(request):
    if request.method == 'POST':
        campo = request.POST.get('campo', '')
        error = request.POST.get('error', '')

        # Aquí puedes realizar cualquier lógica adicional según tus necesidades
        # Puedes registrar los errores, realizar otras acciones, etc.

        return JsonResponse({'success': False, 'campo': campo, 'error': error})

    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405) 