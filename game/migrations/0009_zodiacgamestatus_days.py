# Generated by Django 5.0.6 on 2024-05-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_remove_zodiacgamestatus_challenger_wanters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zodiacgamestatus',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]