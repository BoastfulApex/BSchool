# Generated by Django 4.2.3 on 2023-07-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_school', '0003_photogallery_videogallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='photogallery',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
