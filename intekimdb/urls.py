from django.urls import path
from . import views

app_name='intekimdb'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    # the main viewing of the site
    path('movies/', views.MovieView.as_view(), name='movie'),
    path('actors/', views.ActorView.as_view(), name='actor'),
    path('awards/', views.AwardView.as_view(), name='award'),
    # THE ADDING MORE content to site
    path('addactors/', views.AddActors.as_view(), name='addactors'),
    path('addmovies/', views.AddMovies.as_view(), name='addmovies'),

]
