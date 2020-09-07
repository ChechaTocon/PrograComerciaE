from django.db import models

# Create your models here.
from django.utils import timezone


class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()#la diferencia es que aqui le pone un text área.
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)#para poder publicar los posts despues
            #blank=true, y null=true sirven para las validaciónes de formularios, en el caso de la fecha de publicación
            #este no se va a exigir al usuario.

#estas tareas son como procedimientos almacenados.
    def publicar(self):#jala los datos de si mismo
        self.fecha_publicacion = timezone.now()#lo único que cambia es la fecha de publicación.
        self.save()

    def __str__(self):#para seleccionar cual de los campos va a mostrar para acceder los detalles del objeto en el panel de control
        return self.titulo
