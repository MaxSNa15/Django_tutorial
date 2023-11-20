from django.shortcuts import render, HttpResponse, redirect
# Importar modelos
from webapp.models import Article
# Importar formularios
from webapp.forms import FormArticle
# Importar sesiones flash
from django.contrib import messages


# Create your views here.
# This is the controller for the webapp app.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

# _________________________________________________________________
def crear_articulo(request, title, content, public):
    # Crear articulo
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    # Guardar articulo
    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def ver_articulo(request, id):
    # Buscar articulo
    try:
        articulo = Article.objects.get(pk=id)
        response = f"Articulo: {articulo.title} - {articulo.content} - {articulo.public}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    # Devolver respuesta
    return HttpResponse(response)

def editar_articulo(request, id, title, content, public):
    # Buscar articulo
    try:
        articulo = Article.objects.get(pk=id)
        # Editar articulo
        articulo.title = title
        articulo.content = content
        articulo.public = public

        # Guardar articulo
        articulo.save()

        response = f"Articulo editado: {articulo.title} - {articulo.content}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def borrar_articulo(request, id):
    # Buscar articulo
    try:
        articulo = Article.objects.get(pk=id) # pk = primary key
        # Borrar articulo
        articulo.delete()
    except:
        pass

    return redirect('articulos')

def articulos(request):
    # Buscar articulos
    #articulos = Article.objects.all()

    #articulos = Article.objects.filter(public=True)

    articulos = Article.objects.filter(public=True).order_by('-id')

    # Devolver respuesta
    return render(request, 'articulos.html', {
        'articulos': articulos
    })

# _________________________________________________________________
def save_article(request):
    """
    # Recoger datos por get
    if request.method == 'GET':
        # Crear articulo
        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        # Guardar articulo
        articulo.save()

        return HttpResponse(f"Articulo creado: {title} - {content} - {public}")
        """
    # Recoger datos por post
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        # Guardar articulo
        articulo.save()

        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} - {articulo.public}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def create_article(request):
    return render(request, 'create_article.html')

# _________________________________________________________________
def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data # Guardar datos del formulario (datos limpios)
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            # Guardar articulo
            articulo.save()

            # Crear Mensaje flash (es una sesion que se borra cuando se recarga la pagina)
            # messages = tipo de mensaje (success, info, warning, error)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            #return HttpResponse(f"{title} - {content} - {public} Guardado correctamente")
            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })