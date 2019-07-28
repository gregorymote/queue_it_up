# Generated by Django 2.2.3 on 2019-07-28 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0020_auto_20190728_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('uri', models.CharField(max_length=500)),
                ('art', models.CharField(max_length=500, null=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Party')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Users')),
            ],
        ),
    ]
