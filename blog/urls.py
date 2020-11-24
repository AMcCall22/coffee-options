from django.urls import path
# from . import views
from .views import BlogView, BlogDetail, AddBlogPost

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('blog_detail/<int:pk>', BlogDetail.as_view(), name="blog-detail"),
    path('add_post/', AddBlogPost.as_view(), name="add-blog-post")
]
