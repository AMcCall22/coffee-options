from django.shortcuts import render, get_object_or_404
from .models import Bean, Country


# Create your views here.

def all_countries(request):
    """ A view to show all countries  """

    countries = Country.objects.all()
    context = {
        'countries': countries,
    }

    return render(request, 'products/countries.html', context)


def bean_detail(request, beans_id):
    """ A view to show individual coffee beans,
        by country and with size options """

    bean = Bean.objects.filter(country=beans_id)

    context = {
        'bean': bean,
    }

    return render(request, 'products/bean_detail.html', context)
