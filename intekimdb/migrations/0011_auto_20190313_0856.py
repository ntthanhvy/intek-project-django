# Generated by Django 2.1.7 on 2019-03-13 01:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intekimdb', '0010_auto_20190312_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('Movies', 'Movies'), ('Actors', 'Actors')], max_length=6)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 1, 56, 48, 663601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 13, 1, 56, 48, 663971, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='award',
            name='actors',
            field=models.ManyToManyField(blank=True, to='intekimdb.Actor'),
        ),
        migrations.AddField(
            model_name='award',
            name='movies',
            field=models.ManyToManyField(blank=True, to='intekimdb.Movie'),
        ),
    ]
