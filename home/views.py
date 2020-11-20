from django.shortcuts import render
from products.models import Region


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def all_regions(request):
    """ A view to show all coffee regions available  """

    regions = Region.objects.all()

    context = {
        'regions': regions,
    }

    return render(request, 'home/index.html', context)
