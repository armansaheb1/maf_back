# Generated by Django 5.0.6 on 2024-05-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_zodiacgamestatus_bomber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zodiacgamestatus',
            name='challenger_wanters',
        ),
        migrations.RemoveField(
            model_name='zodiacgamestatus',
            name='died',
        ),
        migrations.RemoveField(
            model_name='zodiacgamestatus',
            name='ocean',
        ),
        migrations.AddField(
            model_name='zodiacgamestatus',
            name='challenger_wanters',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zodiacgamestatus',
            name='died',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zodiacgamestatus',
            name='ocean',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
