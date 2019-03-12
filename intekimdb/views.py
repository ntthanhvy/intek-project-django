from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from .models import Movie, Actor
from .forms import ActorForm, MovieForm
# Create your views here.




class ActorListView(ListView):
    model = Actor
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorDetailView(DetailView):
    model = Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorCreate(CreateView):
    form_class = ActorForm
    success_url = reverse_lazy('intekimdb:actor_list')
    template_name = 'intekimdb/actor_form.html'    


class ActorUpdate(UpdateView):
    model = Actor
    fields = '__all__'
    template_name_suffix = '_update_form'


class ActorDelete(DeleteView):
    model = Actor
    success_url = reverse_lazy('intekimdb:actor_list')


class MovieListView(ListView):
    model = Movie
    paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'intekimdb/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieCreate(CreateView):
    form_class = MovieForm
    success_url = reverse_lazy('intekimdb:movie_list')
    template_name = 'intekimdb/movie_form.html'


class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'
    template_name_suffix = '_update_form'


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('intekimdb:movie_list')


class IndexView(TemplateView):
    template_name = 'home.html'

