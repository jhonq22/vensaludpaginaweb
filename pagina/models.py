from django.db import models
from django.db.models.signals import pre_save
from web.utils import unique_slug_generator
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=80, verbose_name='Categoria')

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'categorias'


class Galerias(models.Model):
    titulo = models.CharField(max_length=80, verbose_name='Nombre Galería')
    slug = models.SlugField(max_length=200, null=True, blank=True)
    imagen_principal = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Publicación')


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ['id']
        db_table = 'galerias'  



class CatalogoGalerias(models.Model):
    galeria = models.ForeignKey(Galerias, on_delete=models.CASCADE)
    imagen_principal = models.ImageField(null=True, blank=True)


    

    class Meta:
        verbose_name = 'Catologo de Galeria'
        verbose_name_plural = 'Catalogo de Galerias'
        ordering = ['id']
        db_table = 'catalogo_galerias'




class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    fecha_publicacion = models.DateTimeField(auto_now_add= True, null=True)
    imagen_principal = models.ImageField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Publicación')


    def __str__(self):
        return self.titulo


    class Meta:
       verbose_name = 'Noticia'
       verbose_name_plural = 'Noticias'
       ordering = ['id']
       db_table = 'noticias'




class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=200)
    status = models.BooleanField(default= True, verbose_name='Estatus')


    def __str__(self):
        return self.nombre_curso


    class Meta:
       verbose_name = 'Curso'
       verbose_name_plural = 'Cursos'
       ordering = ['id']
       db_table = 'cursos'


class NivelAcademico(models.Model):
    nivel_academico = models.CharField(max_length=200)
    status = models.BooleanField(default= True, verbose_name='Estatus')


    def __str__(self):
        return self.nivel_academico


    class Meta:
       verbose_name = 'Nivel Academicos'
       verbose_name_plural = 'Nivel Academicos'
       ordering = ['id']
       db_table = 'nivel_academicos'


class Estados(models.Model):
    estado = models.CharField(max_length=200)
    status = models.BooleanField(default= True, verbose_name='Estatus')


    def __str__(self):
        return self.estado


    class Meta:
       verbose_name = 'Estado'
       verbose_name_plural = 'Estados'
       ordering = ['id']
       db_table = 'estados'    


   

class Municipios(models.Model):
    municipio = models.CharField(max_length=200)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.municipio


    class Meta:
       verbose_name = 'Municipio'
       verbose_name_plural = 'Municipios'
       ordering = ['id']
       db_table = 'municipios' 





class FormularioIncripcion(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=8)
    archivo_cedula = models.ImageField(null=True, blank=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    profesion = models.CharField(max_length=70)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipios, on_delete=models.CASCADE)
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name='Telefono' )
    telefono_local = models.IntegerField(verbose_name='Telefono Local' )
    correo_electronico = models.EmailField()
    curriculum = models.ImageField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add= True, null=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Registrado')


    def __str__(self):
        return self.cedula


    class Meta:
       verbose_name = 'Formulario de Inscripción'
       verbose_name_plural = 'Formulario de Inscripción'
       ordering = ['id']
       db_table = 'formulario_inscripcion'



class FormularioTecnicos(models.Model):
    cedula = models.CharField(max_length=8)
    archivo_cedula = models.ImageField(null=True, blank=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    profesion = models.CharField(max_length=70)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipios, on_delete=models.CASCADE)
    direccion = models.TextField(verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name='Telefono')
    telefono_local = models.IntegerField(verbose_name='Telefono Local')
    correo_electronico = models.EmailField()
    curriculum = models.ImageField(null=True, blank=True)
    institucion_educativa = models.CharField(null=False, blank=False, max_length=50)
    trabajo = models.BooleanField(null=False, blank=False, default=True)
    tipo_ente = models.CharField(null=True, blank=True, max_length=50)
    ente_trabajador = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add= True, null=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Registrado')


    def __str__(self):
        return self.cedula


    class Meta:
       verbose_name = 'Formulario Para Tecnicos'
       verbose_name_plural = 'Formulario Para Tecnicos'
       ordering = ['id']
       db_table = 'formulario_tecnicos'








def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Noticias)




def slug_generator_2(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator_2, sender=Galerias)