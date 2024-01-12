from django.db import models
from django_countries.fields import CountryField
from django_countries import Countries
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class G8Countries(Countries):
    only = [
        "CA", "FR", "DE", "IT", "JP", "RU", "GB"
    ]
class AfricanCountries(Countries):
    only = settings.COUNTRIES_AFRICA

class Vote(models.Model):
    country = CountryField(countries=G8Countries)
    approve = models.BooleanField()

class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.TextField(max_length=5)
    slug = models.TextField(null=True)

    def __str__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
       
        super().save()