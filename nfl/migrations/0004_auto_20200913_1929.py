# Generated by Django 3.0.5 on 2020-09-13 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0003_auto_20200913_1912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NFL',
            new_name='Teams',
        ),
    ]
