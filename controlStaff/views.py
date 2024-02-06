from django.shortcuts import render #funciones de django
from .forms import StaffForm #traer el formulario de staff de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Staff #importa el modelo de staff de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Staff creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar_staff') # Redirige a la página de listado de los staff
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = StaffForm()  # Crea un objeto vacío 
    return render(request, 'listar_staff', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los staff
def listar_staff(request): #hacemos la solicitud al servidor con la funcion request
    staffs = Staff.objects.all() #mostramos los staff almacenaso en la base de datos
    return render (request, "control-staff.html", {"staffs":staffs}) #respuesta del servidor en la pagina control-staff

#funcion para actualizar o modificar los datos del staff
def update_staff(request, id_staff): #obtener los datos del staff mediante el id
    staff = get_object_or_404(Staff, id_staff=id_staff)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = StaffForm(request.POST, instance=staff) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar_staff') #se regresa al la pagina donde estan los staff
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre': staff.nombre,
            'telefono': staff.telefono,
            'departamento': staff.departamento,
            'username':staff.username,
            'password':staff.password,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_staff(request, id_staff):
    if request.method == 'POST':
        try:
            staff = get_object_or_404(Staff, id_staff=id_staff) 
            staff.delete()
            return JsonResponse({'message': 'Staff eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion