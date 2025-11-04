from django.shortcuts import get_object_or_404, render
from .forms import EditarFotoForm, FotoForm
from django.shortcuts import redirect
from .models import Fotos
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    fotos = Fotos.objects.all()
    return render(request, 'Album/album.html', {'fotos': fotos})

@login_required
def crear_imagen(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = FotoForm()

    return render(request, 'Album/crearFoto.html', {'form': form})

@login_required
def eliminar_imagen(request, id):
    foto = get_object_or_404(Fotos, id=id)
    if request.method == 'POST':
        foto.delete()
        messages.success(request, 'Imagen eliminada del álbum correctamente')
        return redirect('/')
    return render(request, 'Album/eliminar.html', {'foto': foto})


@login_required
def cargar_imagen(request, id):
    foto = get_object_or_404(Fotos, id=id)
    form = EditarFotoForm(instance=foto)
    return render(request, 'Album/editar.html', {'form': form, 'foto': foto})

@login_required
def editar_imagen(request, id):
    foto = get_object_or_404(Fotos, id=id)
    if request.method == 'POST':
        form = EditarFotoForm(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagen actualizada correctamente')
            return redirect('/')
    else:
        form = EditarFotoForm(instance=foto)
    return render(request, 'Album/editar.html', {'form': form, 'foto': foto})