from django.urls import path
from AppBlog.views import * #trae todas las funciones de views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('inicio/',inicio, name="Inicio"),
    path('nosotros', nosotros, name = 'Nosotros'),
    
    
    path('login', login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppBlog/Autenticar/logout.html'), name='Logout'),
    path('register', register, name = 'Register'),
    path("editarUsuario", editarUsuario, name="Editar Usuario"),
    
    
    
    path('addReseña', addReseña, name='Añadir Reseña'),
    path('Reseñas', Reseñas, name='Reseñas'),
    path('buscar/', buscar),
    
    path('Novedades', novedades, name='Novedades'),
    path('AñadirNovedades', addNovedades, name='AñadirNovedades'),
    path("editarNovedad/<novedad_titulo>", editarNovedad, name="Editar Libro"),
    path('borrarNovedades/<novedad_titulo>', borrarNovedades, name='borrarNovedades'),
]


