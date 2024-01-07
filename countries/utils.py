from .models import Country
from django_countries import Countries
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
from django.conf import settings

def searchCountries(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    countries = [country._asdict() for country in Countries()]
    for country in countries:
            country['slug'] = 'congo-dr' if country['code'] =='CD' else slugify(country['name'])
    # countries = countries.distinct().filter(
    #     Q(name__icontains=search_query) |
    #     Q(code__icontains=search_query) 
    # ) 
    return countries, search_query