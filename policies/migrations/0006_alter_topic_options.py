# Generated by Django 5.0.1 on 2024-01-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0005_alter_vote_policy_alter_topic_options_topic_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-vote_ratio', '-vote_total', 'name']},
        ),
    ]
