from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_beans, name='beans'),
    path('<beans_id>', views.bean_detail, name='bean_detail'),
]
