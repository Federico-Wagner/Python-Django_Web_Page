# Generated by Django 4.0 on 2021-12-27 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 9, 25, 57, 272368), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
