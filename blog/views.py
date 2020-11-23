from django.views.generic import ListView, DetailView
from .models import Post

# Codemy


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'
