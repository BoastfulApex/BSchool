# Generated by Django 4.2.3 on 2023-09-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_school', '0006_remove_videogallery_video1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadership',
            name='facebook',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='leadership',
            name='instagram',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
