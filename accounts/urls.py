from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('user/', views.UserView.as_view(), name='account')
]