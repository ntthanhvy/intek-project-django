from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from .models import Movie, Actor, Award
from .forms import ActorForm, MovieForm



# -----------Actor view---------------
class ActorListView(ListView):
    '''
    View list of actors including: actor's name, birthday, gender, 
    nationality.
    '''
    model = Actor
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorDetailView(DetailView):
    '''
    View detail of an actor
    '''
    model = Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorCreate(CreateView):
    '''
    View to create a new actor
    '''
    form_class = ActorForm
    success_url = reverse_lazy('intekimdb:actor_list')  


class ActorUpdate(UpdateView):
    '''
    View to update a specific actor
    '''
    model = Actor
    fields = '__all__'
    template_name_suffix = '_update_form'


class ActorDelete(DeleteView):
    '''
    Detele an an actor
    '''
    model = Actor
    success_url = reverse_lazy('intekimdb:actor_list')


# ---------Movie views---------------------------------
class MovieListView(ListView):
    '''
    View list of movies
    '''
    model = Movie
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetailView(DetailView):
    '''
    View detail of a specific movie
    '''
    model = Movie
    template_name = 'intekimdb/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieCreate(CreateView):
    '''
    view create a movie
    '''
    form_class = MovieForm
    success_url = reverse_lazy('intekimdb:movie_list')
    template_name = 'intekimdb/movie_form.html'


class MovieUpdate(UpdateView):
    '''
    View to update a specific movie
    '''
    model = Movie
    fields = '__all__'
    template_name_suffix = '_update_form'


class MovieDelete(DeleteView):
    '''
    Delete a movie
    '''
    model = Movie
    success_url = reverse_lazy('intekimdb:movie_list')


# ---------------Award views---------------------------------
class AwardListView(ListView):
    '''
    View of all awards
    '''
    model = Award
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AwardDetailView(DetailView):
    '''
    View detail of a specidfic award
    '''
    model = Award
    template_name = 'intekimdb/award_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AwardCreate(CreateView):
    '''
    View create a new award
    '''
    model = Award
    fields = '__all__'
    success_url = reverse_lazy('intekimdb:award_list')


class AwardUpdate(UpdateView):
    '''
    View update an awards
    '''
    model = Award
    fields = '__all__'
    template_name_suffix = '_update_form'


class AwardDelete(DeleteView):
    '''
    Delete an award
    '''
    model = Award
    success_url = reverse_lazy('intekimdb:award_list')


# ------------The home view---------------
class IndexView(TemplateView):
    template_name = 'home.html'

