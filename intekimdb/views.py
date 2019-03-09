from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .forms import ActorForm, MovieForm
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('Hello')


class AddActors(View):
    def get(self, request):
        form = ActorForm()
        return render(request, 'intekimdb/add_actors.html', {'f': form})

    def post(self, request):
        g = ActorForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Saved')
        else:
            return HttpResponse(g)

class AddMovies(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'intekimdb/add_movies.html', {'f': form})

    def post(self, request):
        g = MovieForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Saved')
        else:
            return HttpResponse('Not validate')


class MovieView(TemplateView):
    template_name = 'movie.html'


class ActorView(TemplateView):
    template_name = 'actor.html'


class AwardView(TemplateView):
    template_name = 'award.html'
    