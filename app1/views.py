from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from django.contrib.auth import logout
from django.shortcuts import render

class Post_view(ListView):
    model = Post
    template_name = 'homepage.html'

class Post_detail(DetailView):
    model = Post
    template_name = 'detailpage.html'
    context_object_name = 'index'

class Create_Post(CreateView):
    model = Post
    template_name = "Createpost.html"
    fields = ['title','text', 'author']
class Edit_view(UpdateView):
    model = Post
    template_name = 'editpage.html'
    fields = ['title','text']
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')