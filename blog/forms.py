from django import forms

from .models import Publicacion

class PublicacionForm(forms.ModelForm):

    class Meta: #sirven para agregarle más información a neustra clase
        model = Publicacion #le decimos de que modelo lo queremos
        fields = ('titulo', 'texto',) #no queremos los demas atributos, ya que tienen que serautomaticos.
        #en fields, tambien se pueden agregar más atributos de la publicación.
