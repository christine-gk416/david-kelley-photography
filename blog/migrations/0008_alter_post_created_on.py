# Generated by Django 3.2.6 on 2021-11-12 23:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211112_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 11, 12, 23, 33, 40, 672060, tzinfo=utc)),
        ),
    ]