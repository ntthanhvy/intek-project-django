# Generated by Django 2.1.7 on 2019-03-13 06:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0013_auto_20190313_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='portrait',
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 6, 8, 46, 172127, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 13, 6, 8, 46, 175584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 13, 6, 8, 46, 172788, tzinfo=utc)),
        ),
    ]
