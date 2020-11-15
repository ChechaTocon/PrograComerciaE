from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Publicacion

class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):#es la primera que se ejecuta automaticamente para ejecutar este test
        autor = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')#se crea un autor
        Publicacion.objects.create(autor = autor, titulo = 'Titulo publicacion', texto = 'Texto de prueba de la publicación')
        #se crea una publicación 
        pass


    def test_titulo_label(self):
        publicacion=Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('texto').verbose_name
        self.assertEquals(field_label,'texto')

    def test_titulo_max_length(self):
        publicacion=Publicacion.objects.get(id=1)
        max_length = Publicacion._meta.get_field('titulo').max_length
        self.assertEquals(max_length,100)#definiendo que el tamaño del titulo sea 100, entonces si no lo es manda una alerta.

    def test_fecha_creacion_label (self):
        publicacion = Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label,'Creado')#verificar que la etiqueta de la fecha de creación sea creado
        #sirve bastante para cuando se trabja de forma colaborativa.