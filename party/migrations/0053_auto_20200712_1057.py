# Generated by Django 3.0.4 on 2020-07-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0052_auto_20200711_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='display',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='structure',
            field=models.CharField(choices=[('{} in the Title', '{} in the Title'), ('Songs that {}', 'Songs that {}'), ('Songs where {}', 'Songs where {}'), ('{} Songs', '{} Songs'), ('Songs with {}', 'Songs with {}'), ('Songs from {}', 'Songs from {}'), ('Songs by {}', 'Songs by {}'), ('{}', '{}')], default='{}', max_length=64),
        ),
    ]
