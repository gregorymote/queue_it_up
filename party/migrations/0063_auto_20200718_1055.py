# Generated by Django 3.0.8 on 2020-07-18 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0062_auto_20200718_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='indicies',
            new_name='indices',
        ),
    ]