# Generated by Django 3.0.5 on 2020-09-13 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0005_auto_20200913_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nfl.Team')),
            ],
        ),
    ]
