# Generated by Django 5.0 on 2024-01-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_alter_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]