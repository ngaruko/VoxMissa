from django_countries import Countries
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
from django.conf import settings
import wikipediaapi
import uuid
import json
import re
from django.core.serializers.json import DjangoJSONEncoder
### test wiki
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents


def searchCountries(request):

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()

    results = [] if not(search_query) else [country for country in Countries() if search_query.casefold() in country.name.casefold()
               or search_query.casefold() in country.code.casefold()]
    
    return results, search_query



ESWATINI = [
    {"name": "African United Democratic Party (AUDP)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Communist Party of Swaziland (CPS)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Economic Freedom Fighters of Swaziland (EFF)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Inhlava Party (previously Inhlava Forum)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Maxter Political Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Ngwane National Liberatory Congress (NNLC)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Ngwane Socialist Revolutionary Party (NGWASOREP)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Owen Murray Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Peoples' United Democratic Movement (PUDEMO)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sive Siyinqaba National Movement", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Swaziland Liberation Movement (SWALIMO)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Swazi Democratic Party (SWADEPA)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Swaziland National Front (SWANAFRO)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Swaziland National Progressive Party (SNPP)", "acronym": "", "leader": "", "ideology": ""}
]

LIBYA = [
    {"name": "National Forces Alliance", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Justice and Construction Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Front Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Wadi al-Hiya Alliance", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Union for Homeland", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Centrist Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Libyan National Democratic Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "The Message", "acronym": "", "leader": "", "ideology": ""},
    {"name": "The Foundation", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Party for Development and Welfare", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Nation & Prosperity", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Authenticity & Renewal", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Authenticity & Progress", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Moderate Umma Assembly", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Libik Watani", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Gathering of Wadi al-Shati", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Moderate Youth Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Libyan List for Freedom & Development", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Coalition of Parties", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Libya the Hope", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Wisdom Party", "acronym": "[1]", "leader": "", "ideology": ""}
]

SUDAN = [
    {"name": "Democratic Unionist Party (Al Hizb Al-Ittihadi Al-Dimuqrati)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Umma Party (Hizb al-Umma)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Umma Party (Reform and Renewal)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Omom Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sudanese Congress Party (SCP or SCoP) (Hizb al-Mu’tamar al-Sudani)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Popular Congress Party (Al-Mu'tamar al-Sha’bi)[1]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sudanese Ba'ath Party (Hizb al-Ba'ath as-Sudani)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sudanese Communist Party (Al-Hizb al-Shuyui al-Sudani)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Arab Socialist Ba'ath Party – Organisation[2]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Arab Socialist Ba'ath Party – Country[3]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Liberal Party of Sudan (Al-Hizb Al-Librali)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Binaa Sudan Party (Hizb Binaa Al Sudan) [1]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Liberal Democrats (Hizb Al-Demokhrateen Al-Ahrar)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Nubian Front of Liberation (Jabhat al-Tahrir al-Nuwbia)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "National Democratic Alliance[4]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sudan National Alliance [2]", "acronym": "", "leader": "", "ideology": ""},
    {"name": "The National Reform Party [3]", "acronym": "", "leader": "", "ideology": ""},

    {"name": "Sudanese Unity National Party (S.U.N. PARTY)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Islamic Socialist Party", "acronym": "", "leader": "", "ideology": ""},
    {"name": "PermissionErrorFree People Party (FPP)", "acronym": "", "leader": "", "ideology": ""},
    {"name": "Sudan Democratic Progressive Party", "acronym": "", "leader": "", "ideology": ""}
]

data =[]
def create_acronym(phrase):
        acronym = ""
        name = re.sub('[^A-Za-z0-9]+', ' ', phrase)
        words = name.split()
        words = [word for word in words if len(word) > 2 and word.isalpha]
        for word in words:
            
            acronym += word[0].upper()
        return acronym

def getData(soup, country):
    country_name = country.name
    print ('checking for....' + country_name)
    match country.name:
        case'Chad' | 'Mali':
          
            uls = []
            header = soup.find('h3') # Start here
            for nextSibling in header.findNextSiblings():
                if nextSibling.name == 'ul':
                    uls.append(nextSibling)
            for ul in uls:
                for li in ul.findAll('i'):
                    el = {"name":li.text, "leader": "", "acronym": create_acronym(li.text), "ideology": "No Data Avalable" }
                    el2 = build_fixture(el, country)
                    data.append(el2)
            # return data 

        case'Eswatini':
            for el in ESWATINI:
                
                el2 = build_fixture(el, country)
                data.append(el2)

                

        case'Libya':
            for el in LIBYA:
                el2 = build_fixture(el, country)
                data.append(el2)

        case'Sudan':
            for el in SUDAN:
                el2 = build_fixture(el, country)
                data.append(el2)

        
def getParties(countries):
    
    for country in countries:
        print('TESTING...' + country.name)
        prefix = country.name
        
        # get the response in the form of html
        if country.name == 'Congo (the Democratic Republic of the)':
            prefix = 'the Democratic Republic of the Congo'
        if country.name == 'Cabo Verde':
            prefix ='Cape Verde'

        if country.name == 'Congo':
            prefix ='the Republic of the Congo'
        
        wikiurl="https://en.wikipedia.org/wiki/List_of_political_parties_in_" + prefix.replace(' ', '_')
        table_class="wikitable sortable jquery-tablesorter"
        response=requests.get(wikiurl)
        print(response.status_code)
        if(response.status_code != 200):
            print('Nothing found for country: ' + country.name)
            return
        

        soup = BeautifulSoup(response.text, 'html.parser')
        if country.name in ['Chad', 'Mali', 'Eswatini', 'Libya', 'Sudan']:
            getData(soup, country)
            continue
        table = soup.find('table',{'class':"wikitable"})
        if table:
            df=pd.read_html(str(table))

            df=pd.DataFrame(df[0])
            df = df.dropna(axis=1, how='all')
            print(df.head())
            df.dropna(axis=1, how='all')
            
            df.rename(columns={ "Abbr.":"acronym", "acronym":"acronym", 'Ideologies': "ideology", 'Ideology': "ideology"})

            if country.name == 'Angola':
                df.rename(columns={ "Party.3":"name", "Party.2": "acronym"}, inplace=True) 
            elif country.name == 'Nigeria':
                df.rename(columns={ "Party.1":"name", "Party.2": "acronym", 'Chairperson':"leader"}, inplace=True)
            elif country.name == 'Liberia' or country.name =='Rwanda':
                df.rename(columns={ "Party.3":"name"}, inplace=True)
            elif country.name == 'Ghana':
                df.rename(columns={ "Name.2":"name"}, inplace=True)
            elif country.name == 'Namibia':
                df.rename(columns={ "Party[2].1":"name"}, inplace=True)
            elif country.name == 'Djibouti':
                df.rename(columns={ "Coalition.1":"name"}, inplace=True)
            elif country.name == 'Congo (the Democratic Republic of the)':
                df.rename(columns={ "Alliance.1":"name"}, inplace=True)
            else :
                df.rename(columns={ "Party.1":"name",
                                "Party.2":"name",
                                    "Abbr.":"acronym",
                                    "Name.1": "name",
                                    "Party/Group.1":"name",
                                    "Party[1].1 ":"name",
                                    "Party[1].1": "name",    
                                    "Main ideology": "ideology",
                                    "Main Ideology": "ideology",
                                    "Ideology": "ideology",
                                    "Leader":"leader",
                                    "Chairperson":"leader", "President":"leader", "Party leader": "leader"}, inplace=True)
            
            if "acronym" not in df.columns:
                df["acronym"] = df["name"].map(lambda x:  create_acronym(x))
            if "ideology" not in df.columns:
                df["ideology"] = df["name"].map(lambda x:    " No Data for " + x[0])
            if "leader" not in df.columns:
                df["leader"] = df["name"].map(lambda x:    " No Data for " + x[0])

            df2 = df[["name", "acronym", "leader", "ideology"]]
            print(df2.head())
            dict_list = df2.to_dict("records")
            for el in dict_list:
                    
                    data.append(build_fixture(el, country))
    
    print(data)

    with open("country2.json", "w") as outfile:
        json.dump(data, outfile, cls=DjangoJSONEncoder)
    
def build_fixture(el, country):
        el2 ={
                    "country":country.code,
                    "name": el["name"],
                    "acronym": el["acronym"],
                    "leader": el["leader"],
                    "ideology": el["ideology"],
                }
        return {
    "model": "parties.party",
    "pk": uuid.uuid4(),
    "fields": el2
  }