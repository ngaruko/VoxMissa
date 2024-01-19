# Generated by Django 5.0 on 2024-01-18 01:38

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_remove_project_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]