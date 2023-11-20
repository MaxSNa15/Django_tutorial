"""AprendiendoDos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importar los settings
from django.conf import settings

from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),

    # _________________________________________________________________
    #path('crear-articulo/', views.crear_articulo, name="crear_articulo"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', views.crear_articulo, name="crear_articulo"),
    #path('ver-articulo/', views.ver_articulo, name="ver_articulo"),
    path('ver-articulo/<int:id>/', views.ver_articulo, name="ver_articulo"),
    #path('editar-articulo/', views.editar_articulo, name="editar_articulo"),
    path('editar-articulo/<int:id>/<str:title>/<str:content>/<str:public>/', views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>/', views.borrar_articulo, name="borrar_articulo"),

    # _________________________________________________________________
    path('save-article/', views.save_article, name="save_article"),
    path('create-article/', views.create_article, name="create_article"),

    # _________________________________________________________________
    path('full-article/', views.create_full_article, name="full_article"),
]



# Configuración para cargar archivos estáticos
if settings.DEBUG: # Si estamos en modo DEBUG
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)