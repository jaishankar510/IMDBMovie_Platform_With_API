# Generated by Django 4.2.15 on 2024-08-25 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_api', '0003_unwatchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unwatchlist',
            name='platform',
        ),
    ]
