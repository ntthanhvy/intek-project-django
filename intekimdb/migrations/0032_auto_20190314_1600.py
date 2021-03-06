# Generated by Django 2.1.7 on 2019-03-14 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0031_auto_20190314_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 9, 0, 38, 76316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 9, 0, 38, 78419, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 9, 0, 38, 75500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 9, 0, 38, 76916, tzinfo=utc)),
        ),
    ]
