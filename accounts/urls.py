from django.urls import path

from . import views

app_name='account'
urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('user/', views.UserView.as_view(), name='account'),
    path('category/', views.CategoryListView.as_view(), name='category')
]