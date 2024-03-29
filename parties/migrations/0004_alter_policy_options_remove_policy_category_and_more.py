# Generated by Django 5.0.1 on 2024-01-23 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_alter_party_country'),
        ('policies', '0004_alter_policy_name_topic_alter_subtopic_policy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='policy',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title'], 'verbose_name_plural': 'policies'},
        ),
        migrations.RemoveField(
            model_name='policy',
            name='category',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='name',
        ),
        migrations.AddField(
            model_name='party',
            name='policies',
            field=models.ManyToManyField(null=True, to='parties.policy'),
        ),
        migrations.AddField(
            model_name='policy',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='policy',
            name='subtopic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='policies.subtopic'),
        ),
        migrations.AddField(
            model_name='policy',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='policies.topic'),
        ),
        migrations.AddField(
            model_name='policy',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
