# Generated by Django 3.2.8 on 2021-11-24 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
