from django.shortcuts import render
from .models import Bean, Country, Region


def all_regions(request):
    """ A view to show all coffee regions available  """

    regions = Region.objects.all()

    context = {
        'regions': regions,
    }

    return render(request, 'products/regions.html', context)


def countries_by_region(request, region_id):
    """ A view to show all regions and the countries within each """
    countries = Country.objects.filter(region=region_id)
    context = {
       'countries': countries,
    }

    return render(request, 'products/countries.html', context)


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
