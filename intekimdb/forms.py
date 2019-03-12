from django import forms
from .models import Actor, Movie, Category
from django.contrib.admin.widgets import AdminDateWidget

class ActorForm(forms.ModelForm):
    
    class Meta:
        model = Actor
        fields = ('firstname', 'lastname', 'birthday', 'sex', 'nationality', 'alive')
        widgets = {
            'birthday': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'datepicker'}),
        }

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'category', 'actors', 'logo')

        widgets = {
            'release_date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'datepicker'}),
            'actor': forms.Select()
        }


