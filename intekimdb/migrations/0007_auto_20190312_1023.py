# Generated by Django 2.1.7 on 2019-03-12 03:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0006_auto_20190312_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 12, 10, 23, 40, 92570)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 10, 23, 40, 92919)),
        ),
    ]
