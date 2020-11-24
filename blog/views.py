from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Codemy

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetail, self).get_context_data(*args, **kwargs)
        data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = data.total_likes()
        context['total_likes'] = total_likes
        return context

class AddBlogPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))



