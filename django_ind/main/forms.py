from .models import Painter, Picture, Gallery
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple


class PainterForm(ModelForm):
    class Meta:
        model = Painter
        fields = ["name", "country"]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Художник'}),
                   'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'Страна'})
                   }


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["name", "genre", "year", "painter", "gallery"]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Картина'}),
                   'genre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Жанр'}),
                   'year': DateInput(attrs={'class': 'form-control', 'placeholder': 'Год'}),
                   'painter': Select(attrs={'class': 'form-control', 'placeholder': 'Художник'}),
                   'gallery': Select(attrs={})
        }


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ["name", "city", "country"]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Галерея'}),
                   'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
                   'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'Страна'})
                   }
