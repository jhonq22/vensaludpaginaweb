from django.contrib import admin
from django.db import models
from .models import Categoria, Noticias, CatalogoGalerias,Galerias, FormularioIncripcion, Estados, Municipios, Cursos, NivelAcademico, FormularioTecnicos

# Register your models here.
admin.site.register(Noticias)
admin.site.register(Categoria)
admin.site.register(CatalogoGalerias)
admin.site.register(Galerias)
admin.site.register(FormularioIncripcion)
admin.site.register(Estados)
admin.site.register(Municipios)
admin.site.register(Cursos)
admin.site.register(NivelAcademico)
admin.site.register(FormularioTecnicos)