from .models import Country
from django_countries import Countries
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
from django.conf import settings

def searchCountries(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()
        print('query:' + search_query + 'no')

    countryss = [country._asdict() for country in Countries()]
    results = [] if not(search_query) else [country for country in Countries() if search_query.casefold() in country.name.casefold()
               or search_query.casefold() in country.code.casefold()]
    # for country in results:
    #     print(country)
    #countries = [(record.name, record.code) for record in Countries() if record.code == "NZ"] #[country for country in Countries().items()]
    # for country in countries:
    #         country['slug'] = 'congo-dr' if country['code'] =='CD' else slugify(country['name'])
    # countries = countrys.filter(
    #     Q(name__icontains=search_query) |
    #     Q(code__icontains=search_query) 
    # ) 
    return results, search_query