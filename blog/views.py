from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# A tutorial from Codemy was followed to provide
# a basis for the blog functionality
# https://www.youtube.com/watch?v=B40bteAMM_M

class BlogView(ListView):
    """ A view to show a list of all blog entries """
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    """ A view to show the detail of a blog entry """
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetail, self).get_context_data(*args, **kwargs)
        data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = data.total_likes()
        context['total_likes'] = total_likes
        return context


def LikeView(request, pk):
    """ A view to allow a website user to like a blog post """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))
