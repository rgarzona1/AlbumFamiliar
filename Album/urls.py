from django.contrib import admin
from django.urls import path, include
from Album.views import home, crear_imagen, eliminar_imagen, editar_imagen, cargar_imagen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='album'),
    path('crear/', crear_imagen, name='crear'),
    path('eliminar/<int:id>/', eliminar_imagen, name='eliminar'),
    path('editar/<int:id>/', editar_imagen, name='editar'),
    path('cargar/<int:id>/', cargar_imagen, name='cargar'),
]