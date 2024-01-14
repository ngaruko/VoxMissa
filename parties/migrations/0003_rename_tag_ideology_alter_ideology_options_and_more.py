# Generated by Django 5.0 on 2024-01-14 21:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_alter_party_country'),
        ('policies', '0013_alter_policy_options_rename_title_policy_name'),
        ('users', '0011_remove_profile_country_alter_profile_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Ideology',
        ),
        migrations.AlterModelOptions(
            name='ideology',
            options={'verbose_name_plural': 'ideologies'},
        ),
        migrations.RenameField(
            model_name='party',
            old_name='demo_link',
            new_name='website',
        ),
        migrations.RemoveField(
            model_name='party',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='party',
            name='source_link',
        ),
        migrations.RemoveField(
            model_name='party',
            name='tags',
        ),
        migrations.AddField(
            model_name='party',
            name='ideologies',
            field=models.ManyToManyField(blank=True, null=True, to='parties.ideology'),
        ),
        migrations.AddField(
            model_name='party',
            name='offial_logo',
            field=models.ImageField(blank=True, default='party_logo.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='party',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='citizen', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representative', to='parties.party')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='policies.policy')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parties.party')),
            ],
            options={
                'verbose_name_plural': 'policies',
            },
        ),
    ]