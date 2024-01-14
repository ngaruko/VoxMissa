from .models import Country
from django_countries import Countries
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
from django.conf import settings
import wikipediaapi
import uuid

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

### test wiki
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

ESWATINI = [
    
    {'Country':'Eswatini', 'Name': 'African United Democratic Party (AUDP)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Communist Party of Swaziland (CPS)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Economic Freedom Fighters of Swaziland (EFF)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Inhlava Party (previously Inhlava Forum)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Maxter Political Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Ngwane National Liberatory Congress (NNLC)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Ngwane Socialist Revolutionary Party (NGWASOREP)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Owen Murray Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': "Peoples' United Democratic Movement (PUDEMO)", 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Sive Siyinqaba National Movement', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Swaziland Liberation Movement (SWALIMO)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Swazi Democratic Party (SWADEPA)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Swaziland National Front (SWANAFRO)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Eswatini', 'Name': 'Swaziland National Progressive Party (SNPP)', 'Acronym': '', 'Leader': '', 'Ideology': ''}
]

LIBYA = [
    {'Country':'Libya', 'Name': 'National Forces Alliance', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Justice and Construction Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'National Front Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Wadi al-Hiya Alliance', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Union for Homeland', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'National Centrist Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Libyan National Democratic Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'The Message', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'The Foundation', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'National Party for Development and Welfare', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Nation & Prosperity', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Authenticity & Renewal', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Authenticity & Progress', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Moderate Umma Assembly', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Libik Watani', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'National Gathering of Wadi al-Shati', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Moderate Youth Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Libyan List for Freedom & Development', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'National Coalition of Parties', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Libya the Hope', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Libya', 'Name': 'Wisdom Party', 'Acronym': '[1]', 'Leader': '', 'Ideology': ''}
]

SUDAN = [
    {'Country':'Sudan', 'Name': 'Democratic Unionist Party (Al Hizb Al-Ittihadi Al-Dimuqrati)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Umma Party (Hizb al-Umma)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Umma Party (Reform and Renewal)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Omom Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudanese Congress Party (SCP or SCoP) (Hizb al-Mu’tamar al-Sudani)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Popular Congress Party (Al-Mu\'tamar al-Sha’bi)[1]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudanese Ba\'ath Party (Hizb al-Ba\'ath as-Sudani)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudanese Communist Party (Al-Hizb al-Shuyui al-Sudani)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Arab Socialist Ba\'ath Party – Organisation[2]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Arab Socialist Ba\'ath Party – Country[3]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Liberal Party of Sudan (Al-Hizb Al-Librali)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Binaa Sudan Party (Hizb Binaa Al Sudan) [1]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Liberal Democrats (Hizb Al-Demokhrateen Al-Ahrar)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Nubian Front of Liberation (Jabhat al-Tahrir al-Nuwbia)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'National Democratic Alliance[4]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudan National Alliance [2]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'The National Reform Party [3]', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudanese Unity National Party (S.U.N. PARTY)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Islamic Socialist Party', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Free People Party (FPP)', 'Acronym': '', 'Leader': '', 'Ideology': ''},
    {'Country':'Sudan', 'Name': 'Sudan Democratic Progressive Party', 'Acronym': '', 'Leader': '', 'Ideology': ''}
]

data =[]

def create_acronym(phrase):
        acronym = ""
        print('ACRONYM>>>>:' + phrase)
        words = phrase.split()
        words = [word for word in words if len(word) > 2 and word.isalpha]
        for word in words:
            acronym += word[0].upper()
        return acronym

def getData(soup, country):
    match country:
        case'Chad' | 'Mali':
          
            uls = []
            header = soup.find('h3') # Start here
            for nextSibling in header.findNextSiblings():
                if nextSibling.name == 'ul':
                    uls.append(nextSibling)
            for ul in uls:
                for li in ul.findAll('i'):
                    el = {'Country':country, 'Name':li.text, 'Leader': '', 'Acronym': create_acronym(li.text) }
                    el2 = build_fixture(el)
                    print(el)
                    data.append(el)
                    return el2
            # return data 

    match country:
        case'Eswatini':
            for country in ESWATINI:
                
                return build_fixture(country)

    match country:
        case'Libya':
            for country in LIBYA:
                #build_fixture(country)
                return build_fixture(country)

    match country:
        case'Sudan':
            for country in SUDAN:
                return build_fixture(country)

        
def getParties(country):
    print('TESTING...' + country)
    prefix = country
    # get the response in the form of html
    if country == 'Congo (the Democratic Republic of the)':
        prefix = 'the Democratic Republic of the Congo'
    if country == 'Cabo Verde':
        prefix ='Cape Verde'

    if country == 'Congo':
        prefix ='the Republic of the Congo'
    
    wikiurl="https://en.wikipedia.org/wiki/List_of_political_parties_in_" + prefix.replace(' ', '_')
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(wikiurl)
    print(response.status_code)
    if(response.status_code != 200):
        print('Nothing found for country: ' + country)
        return
    
    #with open("wiki.html") as fp:
    #text = ''.join(letter for letter in response.text if letter.isalnum())
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table',{'class':"wikitable"})
    if table:
        df=pd.read_html(str(table))
    else:
        print('No table found for: ' + country)
        return getData(soup, country)
        
        

    df=pd.DataFrame(df[0])
    df = df.dropna(axis=1, how='all')
    print(df.head())
    df.dropna(axis=1, how='all')
    
    df.rename(columns={ "Abbr.":"Acronym"})
    if country == 'Angola':
        df.rename(columns={ "Party.3":"Name", "Party.2": 'Acronym'}, inplace=True) 
    elif country == 'Nigeria':
        df.rename(columns={ "Party.1":"Name", "Party.2": 'Acronym', 'Chairperson':'Leader'}, inplace=True)
    elif country == 'Liberia' or country =='Rwanda':
        df.rename(columns={ "Party.3":"Name"}, inplace=True)
    elif country == 'Ghana':
        df.rename(columns={ "Name.2":"Name"}, inplace=True)
    elif country == 'Namibia':
        df.rename(columns={ "Party[2].1":"Name"}, inplace=True)
    elif country == 'Djibouti':
        df.rename(columns={ "Coalition.1":'Name'}, inplace=True)
    elif country == 'Congo (the Democratic Republic of the)':
        df.rename(columns={ "Alliance.1":'Name'}, inplace=True)
    else :
        df.rename(columns={ "Party.1":"Name",
                           "Party.2":"Name",
                            "Name.1": "Name",
                            'Party/Group.1':'Name',
                            'Party[1].1 ':'Name',
                            'Party[1].1': 'Name',
                            'Ideologies': 'Ideology', 
                            'Main ideology': 'Ideology',
                            'Chairperson':'Leader', 'President':'Leader', 'Party leader': 'Leader'}, inplace=True)
    #print(df.head())
    if 'Acronym' not in df.columns:
        df['Acronym'] = df['Name'].map(lambda x:  create_acronym(x))
    if 'Ideology' not in df.columns:
        df['Ideology'] = df['Acronym'].map(lambda x:  str(x) + "'s Ideology")
    if 'Leader' not in df.columns:
        df['Leader'] = df['Acronym'].map(lambda x:  str(x) + "'s Leader")
    # if 'Ideology' not in df.columns:
    #     df['Ideology'] = df['Name'].map(lambda x:  str(x) +'Not available')

    #check columns
    cols =[]
    indexes = ['Name', 'Acronym', 'Leader', 'Ideology']
    for i in indexes:
        if i in df.columns:
            cols.append(i) 

    print(cols)  

    df2 = df[cols]
    
    dict_list = df2.to_dict('records')
    for el in dict_list:
        el["Country"] = country
        el["Name"] = ''.join(letter for letter in el['Name'] if letter.isalnum())
        
        return build_fixture(el)
      
    # print(data)
    # return data  

def build_fixture(el):
    return {
    "model": "parties.party",
    "pk": uuid.uuid4(),
    "fields": el
  }