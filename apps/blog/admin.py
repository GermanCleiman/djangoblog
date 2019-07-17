from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# para usar el impor-export creo la clase y agrego  resource_class en CategoriaAdmin
# y como atributo ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    # agrego barra de busqueda en el ModelAdmin que debe estar unida al registro del modelo
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # agrego barra de busqueda en el ModelAdmin que debe estar unida al registro del modelo
    search_fields = ['nombre']
    list_display = ('nombre', 'apellidos', 'estado','fecha_creacion', 'correo',)
    resource_class = AutorResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # agrego barra de busqueda en el ModelAdmin que debe estar unida al registro del modelo
    search_fields = ['titulo', 'slug', 'descripcion']
    list_display = ('titulo', 'slug', 'descripcion','fecha_creacion')
    resource_class = PostResource



# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)# aca se une
admin.site.register(Autor, AutorAdmin)# aca se une
admin.site.register(Post, PostAdmin)
admin.site.register(Trabajador)
admin.site.register(Servicios)
admin.site.register(Trabajo)
