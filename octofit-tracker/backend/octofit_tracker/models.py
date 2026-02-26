"""
Django models for Octofit Tracker collections: User, Team, Activity, Leaderboard, Workout
"""
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(Team, related_name='workouts')
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
