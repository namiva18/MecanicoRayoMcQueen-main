from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('quiensomos/', views.quiensomos, name='quiensomos'),
    path('trab_real/', views.trab_real, name='trab_real'),
    path('caja_cambio/', views.caja_cambio, name='caja_cambio'),
    path('electro/', views.electro, name='electro'),
    path('suspension/', views.suspension, name='suspension'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('registro/', views.registro, name='registro'),
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicaciones/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('publicaciones/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('publicaciones/<int:pk>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('publicaciones/<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),

]