from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Album/album.html')

def crear_imagen(request):
    if request.method == 'POST':
        form = FotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Album/album.html')
    else:
        form=FotoForm()

    return render(request, 'Album/crearFoto.html', {'form': form})

