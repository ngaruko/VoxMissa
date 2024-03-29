# Generated by Django 5.0.1 on 2024-01-19 23:56

import django.db.models.deletion
import django_countries.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('policies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('name', models.CharField(max_length=200)),
                ('acronym', models.CharField(blank=True, max_length=10, null=True)),
                ('leader', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('official_logo', models.ImageField(blank=True, default='party_logo.jpg', null=True, upload_to='')),
                ('website', models.CharField(blank=True, max_length=2000, null=True)),
                ('ideology', models.CharField(blank=True, max_length=200, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='parties.tag')),
            ],
            options={
                'verbose_name_plural': 'parties',
                'ordering': ['-vote_ratio', '-vote_total', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='citizen', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representative', to='parties.party')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parties.party')),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='policies.policy')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parties.party')),
            ],
            options={
                'verbose_name_plural': 'policies',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parties.party')),
                ('voter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='party_voter', to='users.profile')),
            ],
            options={
                'unique_together': {('voter', 'party')},
            },
        ),
    ]
