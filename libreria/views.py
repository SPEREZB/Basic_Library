import json
from tkinter import image_names
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from .models import Libro
from .forms import LibroForm 
from django.views import View
# Create your views here. 
def inicio(request):
    return render(request,'paginas/inicio.html') 
  
def nosotros(request):
   return render(request,'paginas/nosotros.html')

def libros(request):
    libros=Libro.objects.all() 
    return render(request,'libros/index.html',{'libros':libros})

def crear(request): 
    formulario= LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros') 
    return render(request,'libros/crear.html',{'formulario':formulario})
  
def editar(request,id):
    libros= Libro.objects.get(id=id)
    formulario= LibroForm(request.POST or None,request.FILES or None,instance=libros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros') 
    return render(request,'libros/editar.html',{'formulario':formulario})
 
def eliminar(request,id):
  libro= Libro.objects.get(id=id)
  libro.delete()
  return redirect('libros')


class LibrosView(View):  
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self):
        libro3= list(Libro.objects.values()) 
        datos3={'message':"Success22",'libro3':libro3} 
        return JsonResponse(datos3)

    def post(self, request): 
        jd= json.loads(request.body)  
        Libro.objects.create(nombre=jd['nombre'],imagenes=jd['imagenes'],descripcion=jd['descripcion'])
        datos= {'message':"Successxx"}
        return JsonResponse(datos) 
 