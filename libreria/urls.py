from django.urls import URLPattern, path
from django import views
from . import views
from .views import LibrosView
from django.conf import settings
 
urlpatterns=[
    path('',views.inicio,name='inicio'),  
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'), 
    path('libros/descargar/<int:libro_id>/', views.descargar, name='descargar'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar') 
] 
 