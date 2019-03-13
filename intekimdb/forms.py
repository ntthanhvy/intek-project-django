from django import forms
from .models import Actor, Movie, Award
from django.contrib.admin.widgets import AdminDateWidget

class ActorForm(forms.ModelForm):
    
    class Meta:
        model = Actor
        fields = ('firstname', 'lastname', 'birthday', 'sex', 'nationality', 'alive', 'portrait')
        widgets = {
            'birthday': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        }

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'category', 'actors', 'logo')

        widgets = {
            'release_date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        }


class AwardForm(forms.ModelForm):

    class Meta:
        model = Award
        fields = ('name', 'kind', 'movies', 'actors', 'date')

        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y', attrs={
                'class': 'datepicker'
            })
        }