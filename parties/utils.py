from .models import Party, Ideology
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateParties(request, parties, results):

    page = request.GET.get('page')
    paginator = Paginator(parties, results)

    try:
        parties = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        parties = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        parties = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, parties


def searchParties(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    ideologies = Ideology.objects.filter(name__icontains=search_query)

    parties = Party.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(acronym__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(leader__icontains=search_query) |
        Q(ideologies__in=ideologies)
    )
    return parties, search_query
