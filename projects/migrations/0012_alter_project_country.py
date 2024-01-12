# Generated by Django 5.0 on 2024-01-10 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_vote'),
        ('projects', '0011_alter_project_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countries.country'),
        ),
    ]
