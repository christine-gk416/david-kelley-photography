# Generated by Django 3.2.6 on 2021-11-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211111_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='friendly_author_name',
            new_name='author_name',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(),
        ),
    ]