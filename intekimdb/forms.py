from django import forms
from .models import Actor, Movie
from django.contrib.admin.widgets import AdminDateWidget

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('firstname', 'lastname', 'birthday', 'sex', 'nationality', 'alive')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form'}),
            'birthday': AdminDateWidget
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'category', 'actors', 'logo')

        widgets = {
            'release_date': AdminDateWidget
        }