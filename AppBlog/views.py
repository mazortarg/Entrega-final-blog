
from django.http import HttpResponse
from django.shortcuts import render

from AppBlog.models import *
from AppBlog.forms import *


# requeridos para el user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# requeridos para el user

#-----------Views de Usuario----------------------------------------------------------------------------------------------------


#Vista para registrarse
def register(request):

    if request.method == 'POST':    #cuando le haga click al botón

        form = RegistroFormulario(request.POST)   #leer los datos   llenados en el formulario

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppBlog/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   #formulario de django que nos permite crear usuarios.
    
    
    return render(request, "AppBlog/Autenticar/registro.html", {'form':form})



#Vista para iniciar sesión
def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "AppBlog/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "AppBlog/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppBlog/Autenticar/login.html", {'form':form})    #vincular la vista con la plantilla de html

#Vista para Editar Usuarios 

@login_required
def editarUsuario(request):

    usuario = request.user #usuario activo (el que ha iniciado sesión)

    if request.method == "POST":    #al presionar el botón

        miFormulario = RegistroFormulario(request.POST) #el formulario es el del usuario

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppBlog/Autenticar/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppBlog/Autenticar/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})

#-----------Views de Usuarios----------------------------------------------------------------------------------------------------


#-----------Views sin login--------------------------------------------------------------------------------------
def inicio(request):

    return render(request, 'AppBlog/inicio.html')

def nosotros(request):

    return render(request, 'AppBlog/nosotros.html')
#-----------Views sin login--------------------------------------------------------------------------------------





#-----------Views de reseñas----------------------------------------------------------------------------------------------------

@login_required
def addReseña(request):

    if request.method == 'POST':

        miFormulario=LibroFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            Lib = Libro(autor=request.user,titulo=informacion['titulo'], año=informacion['año'],
             autorLib=informacion['autorLib'], puntaje=informacion['puntaje'], reseña=informacion['reseña'])
 
            Lib.save()

            return render(request, 'AppBlog/inicio.html')
    else:

        miFormulario=LibroFormulario()

    return render(request, 'AppBlog/Reseñas/añadirReseña.html', {'form':miFormulario})

@login_required
def buscar(request):

    if request.GET["reseña"]:

        titulo=request.GET['reseña']

        resultados=Libro.objects.filter(titulo__icontains=titulo)

        return render(request, "Appblog/Reseñas/resultadosBusqueda.html",{"resultados":resultados, "busqueda":titulo})

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)


def Reseñas(request):

    lib = Libro.objects.all()

    return render(request, "AppBlog/Reseñas/listadoReseñas.html",{'resultados':lib})
    
#-----------Views de reseñas----------------------------------------------------------------------------------------------------


#-----------Views de Novedades----------------------------------------------------------------------------------------------------

@login_required
def addNovedades(request):

    if request.method == 'POST':

        miFormulario=NovedadesFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            libro = Novedad(titulo=informacion['titulo'], año=informacion['año'],imagen=informacion['imagen'])

            libro.save()

            return render(request, 'AppBlog/inicio.html')
    else:

        miFormulario=NovedadesFormulario()

    return render(request, 'AppBlog/Novedades/añadirNovedad.html', {'form':miFormulario})


@login_required
def novedades(request):

    Novedades = Novedad.objects.all()

    return render(request, "AppBlog/Novedades/listaNovedades.html",{'resultados':Novedades})

@login_required
def borrarNovedades(request, novedad_titulo):

    libro = Novedad.objects.get(titulo=novedad_titulo)
    
    libro.delete()
    
    novedad = Novedad.objects.all()

    return render(request, "AppBlog/Novedades/listaNovedades.html",{'resultados':novedad})

@login_required
def editarNovedad(request, novedad_titulo):

    lib = Novedad.objects.get(titulo=novedad_titulo)

    if request.method == "POST":

        miFormulario = NovedadesFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            lib.titulo = informacion['titulo']
            lib.año = informacion['año']
            lib.imagen = informacion['imagen']

            lib.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario= NovedadesFormulario(initial={'titulo':lib.titulo, 'año':lib.año,'imagen':lib.imagen})

    return render(request, "AppBlog/Novedades/editarNovedades.html",{'miFormulario':miFormulario, 'resultado':novedad_titulo})



#-----------Views de Novedades----------------------------------------------------------------------------------------------------