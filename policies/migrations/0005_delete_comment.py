# Generated by Django 5.0 on 2023-12-24 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0004_rename_topic_subtopic_rename_topics_policy_subtopics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]