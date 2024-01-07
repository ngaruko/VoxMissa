# Generated by Django 5.0 on 2024-01-07 03:51

import countries.models
import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0009_subtopic_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='owner',
        ),
        migrations.AddField(
            model_name='policy',
            name='country',
            field=django_countries.fields.CountryField(countries=countries.models.G8Countries, max_length=2, null=True),
        ),
    ]