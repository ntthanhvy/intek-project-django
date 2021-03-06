# Generated by Django 2.1.7 on 2019-03-14 02:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0026_auto_20190313_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 2, 55, 49, 360339, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 2, 55, 49, 362443, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 2, 55, 49, 359567, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 2, 55, 49, 360806, tzinfo=utc)),
        ),
    ]
