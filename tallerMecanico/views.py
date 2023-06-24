from django.shortcuts import render
from .forms import ContactoForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from .forms import PublicacionForm

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'tallerMecanico/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'tallerMecanico/detalle_publicacion.html', {'publicacion': publicacion})

def nueva_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm()
    return render(request, 'tallerMecanico/nueva_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            publicacion = form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'tallerMecanico/editar_publicacion.html', {'form': form})

def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'tallerMecanico/eliminar_publicacion.html', {'publicacion': publicacion})

def index(request):
    context={}
    return render(request, 'tallerMecanico/index.html', context)

def quiensomos(request):
    context={}
    return render(request, 'tallerMecanico/quiensomos.html', context)

def trab_real(request):
    context={}
    return render(request, 'tallerMecanico/trab_real.html', context)

def caja_cambio(request):
    context={}
    return render(request, 'tallerMecanico/caja_cambio.html', context)

def electro(request):
    context={}
    return render(request, 'tallerMecanico/electro.html', context)

def suspension(request):
    context={}
    return render(request, 'tallerMecanico/suspension.html', context)



@csrf_protect
def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            context = {'mensaje': "good"}
        else:
            context = {'error': "bad"}
    else:
        formulario = ContactoForm()
        context = {'form': formulario}

    return render(request, 'tallerMecanico/contacto.html', context)

def login(request):
    context={}
    return render(request, 'tallerMecanico/login.html', context)
                  
def plantilla(request):
    context={}
    return render(request, 'tallerMecanico/plantilla.html', context)

def registro(request):
    context={}
    return render(request, 'tallerMecanico/registro.html', context)

                  