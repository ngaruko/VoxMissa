from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django_countries import Countries
from parties.models import Party
from projects.models import Project
from django.db.models import Q

from users.models import Profile
from django.utils.text import slugify
from policies.models import Topic
import json
import uuid

from django.core.serializers.json import DjangoJSONEncoder

###
from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import getElections, searchCountries, getParties              


africa  = [country for country in Countries() if country.code in ['AO', 'BF', 'BI', 'BJ', 'BW', 'CD', 'CF', 'CG', 'CI', 'CM', 'CV', 'DJ', 'DZ', 'EG', 'ER', 'ET', 'GA', 'GH',
        'GM', 'GN', 'GQ', 'GW', 'KE', 'KM', 'LS', 'LR', 'LY', 'MA', 'MG', 'ML', 'MR', 'MU', 'MW', 'MZ', 'NA', 'NE', 'NG', 'RW',
        'SC', 'SD', 'SL', 'SN', 'SO', 'SS', 'ST', 'SZ', 'TD', 'TG', 'TN', 'TZ', 'UG', 'ZA', 'ZM', 'ZW' ]]
    
america = [country for country in Countries() if country.code in ['AG', 'AR', 'BS', 'BB', 'BZ', 'BM', 'BO', 'BR', 'CA', 'CL', 'CO', 'CR', 'CU', 'DM', 'DO', 'EC', 'SV', 'GD', 'GT', 
            'GY', 'HT', 'HN', 'JM', 'MX', 'NI', 'PA', 'PY', 'PE', 'PR', 'KN', 'LC', 'VC', 'SR', 'TT', 'US', 'UY', 'VE'
            ]]
              
asia  = [country for country in Countries() if country.code in ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CY', 'GE', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 
        'KW', 'KG', 'LA', 'LB', 'MY', 'MV', 'MN', 'MM', 'NP', 'KP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY',
        'TW', 'TJ', 'TH', 'TR', 'TM', 'AE', 'UZ', 'VN', 'YE'
        ]]

europe = [country for country in Countries() if country.code in ['AL', 'AD', 'AM', 'AT', 'AZ', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'GE', 'DE', 'GR',
            'HU', 'IS', 'IE', 'IT', 'KZ', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU',
            'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 'GB', 'VA'
            ]]

oceania = [country for country in Countries() if country.code in ['AS', 'AU', 'FJ', 'FM', 'KI', 'MH', 'NR', 'NZ', 'PW', 'PG', 'SB', 'TO', 'TV', 'VU', 'WS'
            ]] 

def home(request):
    results, search_query = searchCountries(request)
    countries = [country for country in Countries()]
      
    context ={ 
        
            'countries': countries,
            'results': results,
            'africa':africa,
            'america':america,
            'asia':asia,
            'europe':europe,
            'oceania':oceania,
            'search_query':search_query
    }

    #getParties(africa)
    #getElections()
    
    # with open('policies.json') as json1:
    #     data = json.load(json1)
    #     for item in data:
    #         item['pk']=uuid.uuid4

    # with open('policies.json', 'w') as json1:
    #     json.dump(data, json1, cls=DjangoJSONEncoder)

    return render(request, 'home.html', context)



def country(request, pk):
    countryObj = [country for country in  Countries() if country.code.casefold() ==pk.casefold()][0] 
    print('Page: ' + countryObj.name)   
    candidates = Profile.objects.all()
    programs = Project.objects.filter(country__name=countryObj.name)
    policies = Project.objects.filter(country__name=countryObj.name)
    parties = Party.objects.filter(country__name=countryObj.name)
    party = parties[9]
    print(party. name + '>>>>' + party.imageURL)
    context = {'countries': Countries(),  'africa' :africa, 'country': countryObj, 'policies': policies, 'projects': programs, 
               'profiles':candidates, 'parties': parties}
    return render(request, 'country.html', context)

def seed(request):
    #Test data scrapped from wikipedia > political parties
    getParties(africa)
    #Party.objects.all().delete()
    return render(request, 'Parties seeded !', { })