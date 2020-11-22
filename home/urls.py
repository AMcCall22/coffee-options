from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.all_regions, name='regions'),
    # path('<int:region_id>/', views.countries_by_region, name='countries_by_region'),
]
