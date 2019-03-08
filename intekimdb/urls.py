from django.urls import path
from . import views

app_name='intekimdb'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('addactors/', views.AddActors.as_view(), name='addactors'),
    path('addmovies/', views.AddMovies.as_view(), name='addmovies'),

]
