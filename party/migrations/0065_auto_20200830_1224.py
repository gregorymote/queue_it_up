# Generated by Django 3.0.8 on 2020-08-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0064_auto_20200830_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='debug',
            field=models.CharField(default='', max_length=4000),
        ),
    ]
