from django.urls import path

from . import views


app_name='intekimdb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('actors/', views.ActorListView.as_view(), name='actor_list'),
    path('actors/create/', views.ActorCreate.as_view(), name='actor_create'),
    path('actors/<int:pk>/', views.ActorDetailView.as_view(), name='actor_detail'),
    path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actor_update'),
    path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actor_delete'),
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('awards/', views.TemplateView.as_view(template_name='award.html'), name='award'),
 
    # path('addactors/', views.AddActors.as_view(), name='addactors'),
    # path('addmovies/', views.MovieCreate.as_view(), name='addmovies'),
    # path('movies/', views.ViewMovies.as_view(), name='viewmovies'),
    # path('movies/<int:pk>', views.DetailMovies.as_view(), name='detail'),
    # path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    # path('movies/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

