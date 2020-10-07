from django.shortcuts import render, HttpResponse, redirect
from.models import Noticias, Galerias, CatalogoGalerias
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import InscripcionForm


def inicio(request):
    return render(request, "inicio.html")

def mision(request):
    return render(request, "mision.html")

def vision(request):
    return render(request, "vision.html")

def quienes_somos(request):
    return render(request, "quienes_somos.html")

def red_nacional_antecedentes(request):
    return render(request, "red_nacional_antecedentes.html")    

def taller_movil_electromedicina(request):
    return render(request, "taller_movil_electromedicina.html")    

def taller_nacional_electromedicina(request):
    return render(request, "taller_nacional_electromedicina.html") 

def youtube(request):
    return render(request, "youtube.html")

def galerias(request):


    galerias = Galerias.objects.filter(id= '2')
    paginator = Paginator(galerias, 2)
    page = request.GET.get('page')
    galerias = paginator.get_page(page)
    context = {"galerias": galerias}
    return render(request, "galerias.html", context)   






  




def noticias(request):
    queryset = request.GET.get("buscar")
    noticias = Noticias.objects.filter(status= True)
    if queryset:
        noticias = Noticias.objects.filter(
           Q(titulo__icontains = queryset ) |
           Q(contenido__icontains = queryset )
        ).distinct()
       
    paginator = Paginator(noticias, 5)
    page = request.GET.get('page')
    noticias = paginator.get_page(page)
    context = {"noticias": noticias}
    return render(request, "noticias.html", context)





def catalogogalerias(request, id):


    catalogos = CatalogoGalerias.objects.filter(galeria_id=id)
    context = {"catalogos": catalogos}
    return render(request, "catalogo_galeria.html", context)   



def post(request, slug_text):
    noticia = Noticias.objects.filter(slug=slug_text)
    if noticia.exists():
        noticia = noticia.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")

    context = {'noticia': noticia}

    return render(request, "post.html", context)    






def crearFormularioInscripcion(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = InscripcionForm(request.POST) # clase de InscripcionForm que esta en el archivo forms.py
        if autor_form.is_valid():
            autor_form.save()
            return redirect('/home/') 
    else :
        autor_form = InscripcionForm() 
        print(autor_form)
    return render(request, 'formulario_inscripcion.html', {'autor_form': autor_form})






