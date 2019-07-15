from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', blank = False, max_length = 100, null = False)
    estado = models.BooleanField('Categoria Activada/Categoria Desactivada', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)
    # auto_now= True Pone la fecha cada vez que se accede, False no
    # auto_now_add=True Solo pone la fecha de creacion, False ó no

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres del Autor', blank = False, max_length = 255, null = False)
    apellidos = models.CharField('Apellidos del Autor', blank = False, max_length = 255, null = False)
    facebook = models.URLField('Facebook', blank = True, null = True)
    twitter = models.URLField('Twitter', blank = True, null = True)
    instagram = models.URLField('Instagram', blank = True, null = True)
    web = models.URLField('Web', blank = True, null = True)
    correo = models.EmailField('Correo electrónico', blank = False, null = False)
    estado = models.BooleanField('Autor Activo/ Autor Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)
# RichTextField agrega en descripcion un menu de edicion de texto
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', blank = False, max_length = 100, null = False)
    slug = models.CharField('Slug', blank = False, max_length = 100, null = False)
    descripcion = models.CharField('Descripcion', blank = False, max_length = 255, null = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length = 255, blank = True, null = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Autor Activo/ Autor Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Trabajador(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres del Autor', blank = False, max_length = 255, null = False)
    apellidos = models.CharField('Apellidos del Autor', blank = False, max_length = 255, null = False)
    correo = models.EmailField('Correo electrónico', blank = False, null = False)
    direccion = models.CharField('Direccion', blank = False, max_length = 255, null = False)
    telefono1 = models.CharField('Telefono 1', blank = False, max_length = 20, null = False)
    telefono2 = models.CharField('Telefono 2', blank = False, max_length = 20, null = False)
    experiencia = RichTextField()
    ofertas = RichTextField()

    estado = models.BooleanField('Autor Activo/ Autor Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)

class Servicios(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres del Autor', blank = False, max_length = 255, null = False)
    apellidos = models.CharField('Apellidos del Autor', blank = False, max_length = 255, null = False)
    correo = models.EmailField('Correo electrónico', blank = False, null = False)
    direccion = models.CharField('Direccion', blank = False, max_length = 255, null = False)
    telefono1 = models.CharField('Telefono 1', blank = False, max_length = 20, null = False)
    telefono2 = models.CharField('Telefono 2', blank = False, max_length = 20, null = False)
    oferta = RichTextField()
    estado = models.BooleanField('Autor Activo/ Autor Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)

class Trabajo(models.Model):
    id = models.AutoField(primary_key = True)
    empresa = models.CharField('Nombres del Autor', blank = False, max_length = 255, null = False)
    nombre = models.CharField('Nombres del Autor', blank = False, max_length = 255, null = False)
    apellidos = models.CharField('Apellidos del Autor', blank = False, max_length = 255, null = False)
    correo = models.EmailField('Correo electrónico', blank = False, null = False)
    direccion = models.CharField('Direccion', blank = False, max_length = 255, null = False)
    telefono1 = models.CharField('Telefono 1', blank = False, max_length = 20, null = False)
    telefono2 = models.CharField('Telefono 2', blank = False, max_length = 20, null = False)
    oferta = RichTextField()
    estado = models.BooleanField('Autor Activo/ Autor Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

    def __str__(self):
        return "{0},{1},{2}".format(self.apellidos, self.nombre, self.empresa)
