from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_regions, name='all_regions'),
    path('<region_id>', views.countries_by_region, name='countries_by_region'),
    path('', views.all_countries, name='countries'),
    path('<beans_id>', views.bean_detail, name='bean_detail'),
]
