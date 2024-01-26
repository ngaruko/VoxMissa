# Generated by Django 5.0.1 on 2024-01-23 08:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_policy_subtopics_alter_subtopic_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='name',
            field=models.CharField(choices=[('JANUARY', 'January'), ('FEBRUARY', 'February'), ('MARCH', 'March'), ('DECEMBER', 'December')], max_length=200),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subtopics', models.ManyToManyField(to='policies.subtopic', verbose_name='list of sites')),
            ],
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policies.topic'),
        ),
    ]
