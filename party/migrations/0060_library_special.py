# Generated by Django 3.0.8 on 2020-07-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0059_party_lib_repo'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
