# Generated by Django 3.0.8 on 2020-08-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0063_auto_20200718_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='debug',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='songs',
            name='debug',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
