# Generated by Django 3.0.4 on 2020-06-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0045_library_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='full',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
