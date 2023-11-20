from django.db import models

        # Create your models here.
"""
    Un modelo es la parte en la que se conecta a la base de datos y esta trabajando e interactuando con ella

    Los modelos van a ser los objetos y entidades que se usan dentro del proyecto
    Cada modelo representa una tabla en la base de datos
    y cada una de las propiedades de ese modelo representan una columna en la tabla
"""

# nombre en singular
# Heredamos de models.Model realmente te crea una tabla en la base de datos
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo") # CharField es un campo de caracteres, max_length es el tamaño maximo de caracteres 
    content = models.TextField(verbose_name="Contenido") # TextField es un campo de texto mucho mas grande que el CharField
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to='articles') # ImageField es un campo de tipo imagen y default es el valor por defecto
    public = models.BooleanField(verbose_name="Publico") # BooleanField es un campo de tipo booleano
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField es un campo de tipo fecha y hora, auto_now_add=True es para que se agregue automaticamente la fecha y hora
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True es para que se actualice automaticamente la fecha y hora
    # verbose_name es para ponerle un nombre mas amigable a la columna en la base de datos
    class Meta:
        verbose_name = 'Articulo' # Ponerle un nombre singular al modelo
        verbose_name_plural = 'Articulos' # Ponerle un nombre plural al modelo
        ordering = ['-id'] # Ordenar los articulos por id de forma descendente

    def __str__(self):
        return f'{self.title} - {self.public}'

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'Categoria' # Ponerle un nombre singular al modelo
        verbose_name_plural = 'Categorias' # Ponerle un nombre plural al modelo
        ordering = ['-id'] # Ordenar los articulos por id de forma descendente