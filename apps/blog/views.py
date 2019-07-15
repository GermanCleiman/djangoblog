from django.shortcuts import render, redirect
from .models import Post, Categoria, Trabajador, Trabajo, Servicios
from django.shortcuts import get_object_or_404
# esto valida la consulta y si no existe manda un 404
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import TrabajadorForm


# Create your views here.

def home (request):
    queryset = request.GET.get('buscar')
    # recupera lo que ponemos en buscar del index barra de busqueda
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
        # si existe un queryset Q busca por titulo ó "|" por
        # descripcion y .distinct() busca que no se repitan

    # paginacion ------------------
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts':posts})

def detallePost(request, slug):
    posts = get_object_or_404(Post, slug = slug)

    return render(request, 'post.html',{'detalle_post': posts})

def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Generales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q ( titulo__icontains = queryset ) |
            Q ( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Generales'),
        ).distinct()
    # si a nombre= le agrego nombre__exact= , busca talcual esta escrito generales
    # si agrego __iexact= no importan las mayusculas o minusculas
    # si agrego __icontains= no importan las mayusculas o minusculas

    # paginacion ------------------
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'busco.html', {'posts':posts})

def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Programacion')
    )
    if queryset:
        posts = Post.objects.filter(
            Q ( titulo__icontains = queryset ) |
            Q ( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion'),
        ).distinct()

        # paginacion ------------------
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

    return render(request, 'trabajo.html', {'posts':posts})

def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Tecnologia')
    )
    if queryset:
        posts = Post.objects.filter(
            Q ( titulo__icontains = queryset ) |
            Q ( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'),
        ).distinct()

        # paginacion ------------------
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

    return render(request, 'comentarios.html', {'posts':posts})

def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q ( titulo__icontains = queryset ) |
            Q ( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'),
        ).distinct()

        # paginacion ------------------
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

    return render(request, 'administracion.html', {'posts':posts})

def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Videojuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q ( titulo__icontains = queryset ) |
            Q ( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'),
        ).distinct()

        # paginacion ------------------
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

    return render(request, 'servicios.html', {'posts':posts})

def trabajador(request):
    trabajador_form = TrabajadorForm(request.POST)
    if trabajador_form.is_valid():
        trabajador_form.save()
        return redirect('blog:index')
    else:
        trabajador_form = TrabajadorForm()
        return render(request,'busco.html', {'trabajador_form':trabajador_form})
