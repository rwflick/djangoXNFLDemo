# Generated by Django 3.0.5 on 2020-09-13 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0002_auto_20200913_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nfl',
            old_name='divisions',
            new_name='division',
        ),
    ]
