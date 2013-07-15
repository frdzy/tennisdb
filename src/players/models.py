from django.db import models

import datetime


class Gender(object):
    UNKNOWN = 'U'
    MALE = 'M'
    FEMALE = 'F'
    CHOICES = (
        (UNKNOWN, 'Unknown'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )


class Player(models.Model):
    ''' Basic info '''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    ''' Age calculation '''
    birthday = models.DateField()

    ''' Gender '''
    gender = models.CharField(
        max_length=1,
        choices=Gender.CHOICES,
        default=Gender.CHOICES[0][0],
    )

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        return datetime.date.today() - self.birthday


class SideType(object):
    SINGLES = 'S'
    DOUBLES = 'D'
    CHOICES = (
        (SINGLES, 'Singles'),
        (DOUBLES, 'Doubles'),
    )


class Side(models.Model):
    players = models.ManyToManyField(Player)

    player_a = models.ForeignKey(Player, related_name='player_a')
    player_b = models.ForeignKey(Player, related_name='player_b', null=True)

    type = models.CharField(
        max_length=1,
        choices=SideType.CHOICES,
        default=SideType.CHOICES[0][0],
    )

    class Meta:
        ''' Maintain uniqueness of pairs by respecting ordering of
            player_a.id < player_b.id
        '''
        unique_together = ('player_a', 'player_b')

