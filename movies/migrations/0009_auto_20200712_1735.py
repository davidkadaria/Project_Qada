# Generated by Django 3.0.7 on 2020-07-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20200712_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='geo_title',
            field=models.CharField(max_length=200),
        ),
    ]
