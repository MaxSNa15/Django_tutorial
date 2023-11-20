from django.contrib import admin

# Importar modelos
from webapp.models import Article, Category

# Register your models here.

# Para poder ver los modelos en el panel de administracion
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # Para que no se puedan editar estos campos

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)


# Configuración del título del panel de administración
TITLE = "Master en Python|Aprendiendo Django"
admin.site.site_header = TITLE
admin.site.site_title = TITLE
admin.site.index_title = "Panel de gestión"