# Generated by Django 3.0.7 on 2020-07-12 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_episode_serie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='film_poster_high',
            new_name='serie_poster_high',
        ),
        migrations.RenameField(
            model_name='serie',
            old_name='film_poster_low',
            new_name='serie_poster_low',
        ),
    ]
