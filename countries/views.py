from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django_countries import Countries
from .models import Country
from django.utils.text import slugify

###
from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import searchCountries


def countries(request):
    countries, search_query = searchCountries(request)
    # countries = [country._asdict() for country in Countries()]
    # for country in countries:
    #         country['slug'] = slugify(country['name'])


    context ={ 
        
            'countries': countries,
             #'search_query': search_query,
        'africa' : ['AO', 'BF', 'BI', 'BJ', 'BW', 'CD', 'CF', 'CG', 'CI', 'CM', 'CV', 'DJ', 'DZ', 'EG', 'ER', 'ES', 'ET', 'GA', 'GH',
        'GM', 'GN', 'GQ', 'GW', 'KE', 'KM', 'LS', 'LR', 'LY', 'MA', 'MG', 'ML', 'MR', 'MU', 'MW', 'MZ', 'NA', 'NE', 'NG', 'RW',
        'SC', 'SD', 'SH', 'SL', 'SN', 'SO', 'SS', 'ST', 'SZ', 'TD', 'TG', 'TN', 'TZ', 'UG', 'ZA', 'ZM', 'ZW' ],
    
            'asia' :[
        'AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CY', 'GE', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 
        'KW', 'KG', 'LA', 'LB', 'MY', 'MV', 'MN', 'MM', 'NP', 'KP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY',
        'TW', 'TJ', 'TH', 'TR', 'TM', 'AE', 'UZ', 'VN', 'YE'
        ],
                'europe' : [
            'AL', 'AD', 'AM', 'AT', 'AZ', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'GE', 'DE', 'GR',
            'HU', 'IS', 'IE', 'IT', 'KZ', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU',
            'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 'GB', 'VA'
            ],
                'america': [
            'AG', 'AR', 'BS', 'BB', 'BZ', 'BM', 'BO', 'BR', 'CA', 'CL', 'CO', 'CR', 'CU', 'DM', 'DO', 'EC', 'SV', 'GD', 'GT', 
            'GY', 'HT', 'HN', 'JM', 'MX', 'NI', 'PA', 'PY', 'PE', 'PR', 'KN', 'LC', 'VC', 'SR', 'TT', 'US', 'UY', 'VE'
            ],
                'oceania': [
            'AS', 'AU', 'FJ', 'FM', 'KI', 'MH', 'NR', 'NZ', 'PW', 'PG', 'SB', 'TO', 'TV', 'VU', 'WS'
            ]
        }   


    return render(request, 'countries/countries.html', context)


def country(request, pk):
    countryObj = Country(slug=pk)

    return render(request, 'countries/country.html', {'country': countryObj})