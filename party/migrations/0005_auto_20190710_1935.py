# Generated by Django 2.2.3 on 2019-07-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_auto_20190708_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
