from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import edit, TemplateView, ListView
from intekimdb.forms import CategoryForm
from intekimdb.models import Category

from django.views.generic.edit import CreateView
# Create your views here.
class Signup(edit.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserView(ListView):
    template_name = 'user.html'
    model = Category
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryListView(CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy('account')
    template_name = 'add_category.html'
    
