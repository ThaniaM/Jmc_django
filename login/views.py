from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es autenticado, iniciar sesión
            login(request, user)
            if user.is_staff and user.is_superuser:
                # El usuario es miembro del grupo "Administrator"
                print("Redireccionando a 'controlCliente' para administrador")
                return redirect('inicioAdmin')
            else:
                # El usuario no es administrador, redirigir a la página de clientes
                print("Redireccionando a 'equipoClientes' para no administrador")
                return redirect('inicioCliente')
        else:
            # El usuario no es autenticado, mostrar un mensaje de error
            messages.error(request, 'El nombre de usuario o contraseña no son correctos.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            # Crear un nuevo usuario
            user = User.objects.create_user(username=username, password=password)
            print(f"Usuario {username} creado exitosamente.")

            # Autenticar al usuario recién creado
            user = authenticate(request, username=username, password=password)
            login(request, user)


        else:
            print(f"El usuario {username} ya existe.")

    return render(request, 'register_user.html')

def logout_user(request):
    # Cerrar sesión del usuario
    logout(request)
    return redirect('login')
