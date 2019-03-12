from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import edit, TemplateView

# Create your views here.
class Signup(edit.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserView(TemplateView):
    template_name = 'user.html'