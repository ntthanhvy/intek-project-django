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
    path('awards/', views.AwardListView.as_view(), name='award_list'),
    path('awards/create/', views.AwardCreate.as_view(), name='award_create'),
    path('awards/<int:pk>/', views.AwardDetailView.as_view(), name='award_detail'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='award_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='award_delete'),
    path('comment/<int:pk>/<int:id>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('comment/<int:pk>/<int:id>/update/', views.CommentUpdate.as_view(), name='comment_update'),

]

