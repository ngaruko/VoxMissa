# Generated by Django 5.0.1 on 2024-01-20 00:22

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_alter_party_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
