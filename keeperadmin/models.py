from django.db import models


class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=25, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Keeper(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(max_length=50, blank=True)
    team = models.CharField(max_length=50, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['lastname','firstname']

    def __str__(self):
        return self.lastname + " " + self.firstname


from django.db import models
from keeperadmin.models import Keeper


class GameStats(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    recording_date = models.DateField(max_length=50, blank=True)
    keeper = models.ForeignKey(Keeper, on_delete=models.CASCADE)
    minutes_played = models.IntegerField(blank=True)
    goals_against = models.IntegerField(blank=True)
    shots_on_goal = models.IntegerField(blank=True)
    saves = models.IntegerField(blank=True)
    total_passes = models.IntegerField(blank=True)
    passes_right = models.IntegerField(blank=True)
    passes_left = models.IntegerField(blank=True)
    passes_successfull = models.IntegerField(blank=True)

    class Meta:
        ordering = ['recording_date', 'keeper']

    def __str__(self):
        return self.keeper

