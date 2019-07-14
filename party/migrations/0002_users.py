# Generated by Django 2.2.3 on 2019-07-07 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('points', models.IntegerField()),
                ('isHost', models.BooleanField()),
                ('hasSkip', models.BooleanField()),
                ('state', models.CharField(max_length=20)),
                ('turn', models.CharField(max_length=20)),
                ('partyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Party')),
            ],
        ),
    ]