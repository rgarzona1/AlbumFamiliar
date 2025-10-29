from django.contrib import admin
from django.urls import path, include
from Album.views import home, crear_imagen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('crear/', crear_imagen),
    
] 