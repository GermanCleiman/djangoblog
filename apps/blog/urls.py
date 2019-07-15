from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    # paso un parametro tipo slug que es cadena
    path('busco/', trabajador, name = 'busco'),
    path('trabajo/', programacion, name = 'trabajo'),
    path('comentarios/', tecnologia, name = 'comentarios'),
    path('administracion/', tutoriales, name = 'administracion'),
    path('servicios/', videojuegos, name = 'servicios'),
    path('<slug:slug>/', detallePost, name="detalle_post"),



]
