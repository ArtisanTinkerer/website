from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'content']