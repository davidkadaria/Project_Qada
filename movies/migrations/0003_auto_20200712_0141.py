# Generated by Django 3.0.7 on 2020-07-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='en_title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='geo_title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
