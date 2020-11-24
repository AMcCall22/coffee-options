from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Codemy

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddBlogPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

