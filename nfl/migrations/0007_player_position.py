# Generated by Django 3.0.5 on 2020-09-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0006_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('QB', 'Quarterback'), ('RB', 'Running Back'), ('FB', 'Fullback'), ('WR', 'Wide Receiver'), ('TE', 'Tight End'), ('C', 'Center'), ('OT', 'Offensive Tackle'), ('OG', 'Offensive Guard'), ('DE', 'Defensive End'), ('DT', 'Defensive Tackle'), ('LB', 'Line Backer'), ('DB', 'Defensive Back'), ('CB', 'Cornerback'), ('S', 'Safety'), ('K', 'Kicker'), ('P', 'Punter'), ('LS', 'Long Snapper'), ('KR', 'Kick Returner'), ('PR', 'Punt Returner')], max_length=25, null=True),
        ),
    ]
