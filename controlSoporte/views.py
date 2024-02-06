from django.shortcuts import render #funciones de django
from .forms import EquipoForm #traer el formulario de Equipo de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Equipo #importa el modelo de Equipo de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from controlCliente .models import Cliente


def create_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            equipo_instance = form.save(commit=False)
            equipo_instance.id_servicio = form.cleaned_data['id_servicio']
            equipo_instance.save() # Guarda los datos en la base de datos
            messages.success(request, 'Soporte creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar_equipo') # Redirige a la página de listado de los servicio
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
            return redirect('listar_equipo') # Redirige a la página de listado de los servicio
    else:
        form = EquipoForm()  # Crea un objeto vacío 
    return render(request, 'control-tickets.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los servicios
def listar_equipo(request): #hacemos la solicitud al servidor con la funcion request
    equipos = Equipo.objects.all() #mostramos los servicio almacenaso en la base de datos
    return render (request, "control-tickets.html", {"equipos":equipos}) #respuesta del servidor en la pagina control-ajuste

#funcion para actualizar o modificar los datos del servicio
def update_equipo(request, id_equipo): #obtener los datos del equipo mediante el id
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = EquipoForm(request.POST, instance=equipo) #se crea el formulario para la validacion
        if form.is_valid():
            equipo_instance = form.save(commit=False)
            equipo_instance.id_cliente = form.cleaned_data['id_cliente']
            equipo_instance.save()#si son validos se guardan 
            data = {
                'message': 'Datos actualizados correctamente',
                'id_servicio': equipo_instance.id_servicio_id,
                'id_cliente': equipo_instance.id_cliente_id,
                } 
            return redirect('listar_equipo') #se regresa al la pagina donde estan los servicios
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'tipo_equipo':equipo.tipo_equipo,
            'procesador':equipo.procesador,
            'uso_disco':equipo.uso_disco,
            'marca':equipo.marca,
            'ram':equipo.ram,
            'ip_local':equipo.ip_local,
            'anydesk':equipo.anydesk,
            'nom_usuario':equipo.nom_usuario,
            'nom_antivirus':equipo.nom_antivirus,
            'vig_antivirus':equipo.vig_antivirus,
            'office':equipo.office,
            'vig_office':equipo.vig_office,
            'descripcion':equipo.descripcion,
            'id_servicio':equipo.id_servicio_id,
            'id_cliente':equipo.id_cliente_id,
  
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_equipo(request, id_equipo):
    #if request.method == 'POST':
        #try:
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo) 
    equipo.delete()
    return JsonResponse({'message': 'Equipo eliminado correctamente'})
        #except Exception as e:
            #return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    #else:
    #return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion


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