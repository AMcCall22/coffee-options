from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.all_regions, name='regions'),
]
