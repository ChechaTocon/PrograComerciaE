from django.urls import path
from . import views
#este es el archivo que se llama desde url de mysite, 
#aqui le tenemos que decir que accion realizar cuando lo invocan.
urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'), #funcion que se encuentra en el archivo views
    #la cual se ejecuta cunado la url esta vacía, asimismo el nombre de la url se llamará publicacion_lista.
    path('publicacion/<int:pk>/', views.publicacion_detalle, name='detalle_publicacion'),
    path('publicacion/nueva', views.publicacion_nueva, name='publicacion_nueva'), #en el nombre es el que tiene coincidir de donde lo llamamos.
    path('publicacion/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
]