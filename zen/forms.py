from django import forms
from .models import Manga

class MangaForm(forms.ModelForm):

    class Meta:
        model = Manga

        fields = [
            "title",
            "author",
            "description",
            "url",
        ]