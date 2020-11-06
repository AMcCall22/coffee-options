from django.shortcuts import render, get_object_or_404
from .models import Bean

# Create your views here.


def all_beans(request):
    """ A view to show all coffee beans """

    beans = Bean.objects.all()

    context = {
        'beans': beans,
    }

    return render(request, 'products/beans.html', context)


def bean_detail(request, beans_id):
    """ A view to show individual coffee bean detail """

    bean = get_object_or_404(Bean, pk=beans_id)

    context = {
        'bean': bean,
    }

    return render(request, 'products/bean_detail.html', context)
