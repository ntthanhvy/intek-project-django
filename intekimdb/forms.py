from django import forms
from .models import Actor, Movie, Award, Comment, Category
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name',)


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

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('entry_comment', )
        readonly_fields=('user', 'release_date')
        widgets = {
            'entry_comment': forms.TextInput(),
        }

    def save(self, comment_object, comment_user):
        comment = Comment()
        comment.entry_comment = self.cleaned_data['entry_comment']
        object_model = ContentType.objects.get_for_model(comment_object)
        comment.content_type = object_model
        comment.object_id = comment_object.id
        comment.user = comment_user
        comment.save()

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # deleted form label
        self.fields['entry_comment'].label = ""        


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry_comment', )
        readonly_fields=('user', 'release_date')
        widgets = {
            'entry_comment': forms.TextInput(attrs={'class': 'form-input'}),
        }
    
