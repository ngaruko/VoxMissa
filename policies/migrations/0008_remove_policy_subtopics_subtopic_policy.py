# Generated by Django 5.0 on 2023-12-24 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0007_remove_subtopic_policy_policy_subtopics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='subtopics',
        ),
        migrations.AddField(
            model_name='subtopic',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policies.policy'),
        ),
    ]