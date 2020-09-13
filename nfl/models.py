from django.db import models

# Create your models here.
class Team(models.Model):

    CONFERENCES = [
        ('AFC', 'American Football Conference'),
        ('NFC', 'National Football Conference')
    ]

    DIVISIONS = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West')
    ]

    location = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    conference = models.CharField(max_length=50, choices=CONFERENCES, null=True)
    division = models.CharField(max_length=50, choices=DIVISIONS, null=True)

    def __str__(self):
        return "{} {}".format(self.location, self.nickname)

class Player(models.Model):

    POSITION = [
        ('QB', 'Quarterback'),
        ('RB', 'Running Back'),
        ('FB', 'Fullback'),
        ('WR', 'Wide Receiver'),
        ('TE', 'Tight End'),
        ('C', 'Center'),
        ('OT', 'Offensive Tackle'),
        ('OG', 'Offensive Guard'),
        ('DE', 'Defensive End'),
        ('DT', 'Defensive Tackle'),
        ('LB', 'Line Backer'),
        ('DB', 'Defensive Back'),
        ('CB', 'Cornerback'),
        ('S', 'Safety'),
        ('K', 'Kicker'),
        ('P', 'Punter'),
        ('LS', 'Long Snapper'),
        ('KR', 'Kick Returner'),
        ('PR', 'Punt Returner')
    ]

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=25, null=True, choices=POSITION)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
