# Generated by Django 2.2.6 on 2019-11-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0039_party_token_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]
