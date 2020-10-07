from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('home/', views.inicio, name="home"),
    path('mision/', views.mision, name="mision"),
    path('vision/', views.vision, name="vision"),
    path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
    path('noticias/', views.noticias, name="noticias"),
    path('red_nacional_antecedentes/', views.red_nacional_antecedentes, name="red_nacional_antecedentes"),
    path('taller_movil_electromedicina/', views.taller_movil_electromedicina, name="taller_movil_electromedicina"),
    path('taller_nacional_electromedicina/', views.taller_nacional_electromedicina, name="taller_nacional_electromedicina"),
    path('youtube/', views.youtube, name="youtube"),
    path('galerias/', views.galerias, name="galerias"),
    path('noticias/<slug:slug_text>', views.post),
    path('galerias/<int:id>', views.catalogogalerias),
    path('formulario_inscripcion/', views.crearFormularioInscripcion, name = 'formulario_inscripcion'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)