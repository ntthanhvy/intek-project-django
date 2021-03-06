# Generated by Django 2.1.7 on 2019-03-13 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0024_auto_20190313_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 13, 47, 49, 972582, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 13, 47, 49, 974679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 13, 47, 49, 973076, tzinfo=utc)),
        ),
    ]
