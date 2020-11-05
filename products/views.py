from django.shortcuts import render
from .models import Bean

# Create your views here.


def all_beans(request):
    """ A view to show all coffee beans """

    beans = Bean.objects.all()

    context = {
        'beans': beans,
    }

    return render(request, 'products/beans.html', context)
