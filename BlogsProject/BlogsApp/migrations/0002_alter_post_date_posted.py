# Generated by Django 5.1.3 on 2024-11-30 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 4, 58, 39, 834381, tzinfo=datetime.timezone.utc)),
        ),
    ]
