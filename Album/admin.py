from django.contrib import admin
from Album.models import Fotos

class FotosAdmin(admin.ModelAdmin):
    list_display =['titulo', 'descripcion', 'fecha','imagen']
 

# Register your models here.
admin.site.register(Fotos, FotosAdmin)
