# Generated by Django 4.2.3 on 2023-09-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_school', '0005_leadership_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogallery',
            name='video1',
        ),
        migrations.RemoveField(
            model_name='videogallery',
            name='video2',
        ),
        migrations.RemoveField(
            model_name='videogallery',
            name='video3',
        ),
        migrations.RemoveField(
            model_name='videogallery',
            name='video4',
        ),
        migrations.RemoveField(
            model_name='videogallery',
            name='video5',
        ),
        migrations.RemoveField(
            model_name='videogallery',
            name='video6',
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video1_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video2_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video3_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video4_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video5_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='video6_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='media_type',
            field=models.TextField(choices=[('media', 'Matbuot xizmati'), ('News', 'Yangilik')]),
        ),
    ]
