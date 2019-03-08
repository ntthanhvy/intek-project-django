# Generated by Django 2.1.7 on 2019-03-07 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 1, 19, 8, 971410)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='intekimdb.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 1, 19, 8, 972408)),
        ),
    ]