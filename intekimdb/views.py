from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic import TemplateView

from .models import Movie, Actor, Award, Comment
from .forms import ActorForm, MovieForm, CommentForm, CommentEditForm



# -----------Comment view---------------
class CommentDelete(DeleteView):
    '''
    Delete a comment
    '''
    model = Comment

    def get_success_url(self):
        if self.request.POST.get("movie_cmt"):
            return reverse_lazy('intekimdb:movie_detail', kwargs={'pk': self.kwargs.get('id')})
        elif self.request.POST.get("actor_cmt"):
            return reverse_lazy('intekimdb:actor_detail', kwargs={'pk': self.kwargs.get('id')})
        elif self.request.POST.get("award_cmt"):
            return reverse_lazy('intekimdb:award_detail', kwargs={'pk': self.kwargs.get('id')})


class CommentUpdate(UpdateView):
    '''
    View to update a specific comment
    '''
    model = Comment
    form_class = CommentEditForm

    def get_object(self, querys_set=None):
        return Comment.objects.get(id=self.kwargs['pk'])

    def get_success_url(self):
        if self.request.POST.get("movie_cmt"):
            return reverse_lazy('intekimdb:movie_detail', kwargs={'pk': self.kwargs.get('id')})
        elif self.request.POST.get("actor_cmt"):
            return reverse_lazy('intekimdb:actor_detail', kwargs={'pk': self.kwargs.get('id')})
        elif self.request.POST.get("award_cmt"):
            return reverse_lazy('intekimdb:award_detail', kwargs={'pk': self.kwargs.get('id')})
        



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


class ActorDetailView(DetailView, FormMixin):
    '''
    View detail of an actor
    '''
    model = Actor
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Actor.objects.get(pk=self.kwargs.get('pk')).comments.all()
        context['edit_comment_form'] = CommentEditForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        p_object = Actor.objects.get(pk=self.kwargs.get('pk'))
        
        if form.is_valid():
            form.save(p_object, request.user)
            return redirect(reverse_lazy('intekimdb:actor_detail', kwargs={'pk': p_object.pk}))


class ActorCreate(CreateView):
    '''
    View to create a new actor
    '''
    form_class = ActorForm
    success_url = reverse_lazy('intekimdb:actor_list')  
    template_name = 'intekimdb/actor_form.html'


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


class MovieDetailView(DetailView, FormMixin):
    '''
    View detail of a specific movie
    '''
    model = Movie
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('intekimdb:movie_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['comments'] = Movie.objects.get(pk=self.kwargs.get('pk')).comments.all()
        context['edit_comment_form'] = CommentEditForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        p_object = Movie.objects.get(pk=self.kwargs.get('pk'))
        if form.is_valid():
            form.save(p_object, request.user)
            return redirect(reverse_lazy('intekimdb:movie_detail', kwargs={'pk': p_object.pk}))


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


class AwardDetailView(DetailView, FormMixin):
    '''
    View detail of a specidfic award
    '''
    model = Award
    form_class = CommentForm
    template_name = 'intekimdb/award_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Award.objects.get(pk=self.kwargs.get('pk')).comments.all()
        context['edit_comment_form'] = CommentEditForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        p_object = Award.objects.get(pk=self.kwargs.get('pk'))
        if form.is_valid():
            form.save(p_object, request.user)
            return redirect(reverse_lazy('intekimdb:award_detail', kwargs={'pk': p_object.pk}))


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

