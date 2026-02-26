from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team.name, 'Test Team')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2026-02-26')
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Test Workout')
        workout.suggested_for.add(team)
        self.assertIn(team, workout.suggested_for.all())

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
