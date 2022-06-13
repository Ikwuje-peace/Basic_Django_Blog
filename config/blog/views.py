from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = "all_post"
    ordering = ['-id']

class CreatePostView(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    # fields = ['title', 'body', 'author']

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'
class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    # fields = ['title', 'body']
    template_name = 'edit.html'
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

