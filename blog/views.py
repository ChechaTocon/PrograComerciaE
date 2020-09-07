from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
# Aquí se ponen las operaciones, las "variables" que se muestran en la vista, aqui
# se hacen las queries.

def publicacion_lista(request):
    publicaciones=Publicacion.objects.filter(
                fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones': publicaciones})#el tercer argumento
    #son las variables de las consultas, tienen que ir entre comillas los nombres que se pasan al html
    #y luego la variable de la funcion.