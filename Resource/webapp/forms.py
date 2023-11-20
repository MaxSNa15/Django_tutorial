from django import forms
from django.core import validators

# Create your forms here.

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        #max_length = 50, # el maximo de caracteres que puede tener el titulo
        #min_length= 2, # el minimo de caracteres que puede tener el titulo
        required = True, # si es requerido o no
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑáéíóúÁÉÍÓÚ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        max_length = 500,
        required = True,
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Contenido',
                'class': 'contenido_form_article'
            }
        ),
        validators=[
            validators.MaxLengthValidator(500, 'El contenido es demasiado largo'),
            validators.RegexValidator('^[A-Za-z0-9ñÑáéíóúÁÉÍÓÚ ]*$', 'El contenido esta mal formado', 'invalid_content')
        ]
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )