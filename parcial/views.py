from django.shortcuts import render, get_object_or_404
from .models import Titulo, Deporte, Galeria, Contenido

def paginaPrincipal(request):
    titulo = Titulo.objects.all()
    deporte = Deporte.objects.all()
    datos = {
        'titulo': titulo,
        'deporte': deporte,
    }
    return render(request, 'index.html', datos)

def var_mas(request, deporte_id):
    deporte = get_object_or_404(Deporte, id=deporte_id)
    titulo = Titulo.objects.all()
    galeria = Galeria.objects.all()
    return render(request, 'galeria.html', {'deporte': deporte, 'titulo': titulo, 'galeria': galeria})

def contenido(request):
    titulo = Titulo.objects.all()
    contenido = Contenido.objects.all()
    deporte = Deporte.objects.all()
    return render(request, 'contenido.html', {'contenido': contenido, 'deporte': deporte, 'titulo': titulo})
