import json
import os
import time
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from django.contrib import messages

from expo import settings
from .models import Autor, Libro
from .forms import LibroForm 
from django.views import View
# Create your views here. 
def inicio(request):
    messages.success(request, '¡BIENVENIDO!')
    return render(request,'paginas/inicio.html') 
  
def nosotros(request):
   return render(request,'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    paginator = Paginator(libros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'libros/index.html', {'page_obj': page_obj})


def cargar_libros_desde_json(request):
    json_path = os.path.join(settings.BASE_DIR, 'libros.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for item in data['library']:
                libro_data = item['book']
                autor, _ = Autor.objects.get_or_create(
                    nombre=libro_data['author']['name']
                )
                
                Libro.objects.create(
                    titulo=libro_data['title'],
                    autor=autor,
                    paginas=libro_data['pages'],
                    genero=libro_data['genre'][0].upper(),
                    portada=libro_data['cover'],
                    sinopsis=libro_data['synopsis'],
                    year=libro_data['year'],
                    isbn=libro_data['ISBN']
                )
            
            return JsonResponse({'status': f'{len(data["library"])} libros cargados'})
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_libros(request):
    libros = Libro.objects.all().select_related('autor')
    data = {
        'library': [
            {
                'book': {
                    'title': libro.titulo,
                    'pages': libro.paginas,
                    'genre': libro.get_genero_display(),
                    'cover': libro.portada,
                    'synopsis': libro.sinopsis,
                    'year': libro.year,
                    'ISBN': libro.isbn,
                    'author': {
                        'name': libro.autor.nombre,
                        'otherBooks': []
                    }
                }
            } for libro in libros
        ]
    }
    return JsonResponse(data)
    
def listar_libros(request):
    # Ruta al archivo JSON
    json_path = os.path.join(settings.BASE_DIR, 'libros.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            libros = [item['book'] for item in data['library']]
            
            # Paginación
            paginator = Paginator(libros, 10)  # 10 libros por página
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            return render(request, 'libros/index.html', {
                'page_obj': page_obj,
                'libros': page_obj.object_list  # Para mantener compatibilidad
            })
    
    except FileNotFoundError:
        return render(request, 'libros/index.html', {
            'error': 'Archivo libros.json no encontrado'
        })
    except Exception as e:
        return render(request, 'libros/index.html', {
            'error': str(e)
        })

def crear(request):
    try:
        formulario= LibroForm(request.POST or None,request.FILES or None)
        if formulario.is_valid():
            messages.success(request, '¡Libro creado exitosamente!')
            formulario.save()
            time.sleep(3)
            return redirect('libros')
        return render(request,'libros/crear.html',{'formulario':formulario})
    except:
        messages.error(request, '¡Hubo un error al crear el libro!')
        return render(request,'libros/crear.html')
  
def editar(request,id):
    libros= Libro.objects.get(id=id)
    formulario= LibroForm(request.POST or None,request.FILES or None,instance=libros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, '¡Libro editado exitosamente!')
        return redirect('libros') 
    return render(request,'libros/editar.html',{'formulario':formulario})
 
def eliminar(request,id):
  libro= Libro.objects.get(id=id)
  libro.delete()
  messages.success(request, '¡Libro eliminado exitosamente!')
  return redirect('libros')

def descargar(request, libro_id):
    print("DESCARGA DESDE FIREBASE")
    return redirect('libros')


class LibrosView(View):  
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self):
        libro3= list(Libro.objects.values()) 
        datos3={'message':"Success",'libro3':libro3}
        return JsonResponse(datos3)

    def post(self, request): 
        jd= json.loads(request.body)  
        Libro.objects.create(nombre=jd['nombre'],imagenes=jd['imagenes'],descripcion=jd['descripcion'])
        datos= {'message':"Success"}
        return JsonResponse(datos) 
 