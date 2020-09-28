from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .forms import PublicacionForm
# Aquí se ponen las operaciones, las "variables" que se muestran en la vista, aqui
# se hacen las queries.

def publicacion_lista(request):
    publicaciones=Publicacion.objects.filter(
                fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones': publicaciones})#el tercer argumento
    #son las variables de las consultas, tienen que ir entre comillas los nombres que se pasan al html
    #y luego la variable de la funcion.

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/publicacion_detalle.html', {'publicacion': publicacion})

def publicacion_nueva(request):
    #como se utilizará lo mismo para editar y pueblicar llamamos a publicación editar.
    if request.method == "POST":
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user #el autor es el que esta logeado en nuestro sistema.
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm()
        return render(request, 'blog/publicacion_editar.html', {'form': form}) 

def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        formulario = PublicacionForm(instance=publicacion)
    return render(request, 'blog/publicacion_editar.html', {'form': formulario})