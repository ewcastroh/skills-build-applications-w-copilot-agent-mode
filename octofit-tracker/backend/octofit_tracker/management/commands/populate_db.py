from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create users
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User(email='captain@marvel.com', username='Captain America', team=marvel),
            User(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User(email='batman@dc.com', username='Batman', team=dc),
            User(email='superman@dc.com', username='Superman', team=dc),
            User(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Swimming', duration=60, date=date.today())

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Strength', description='Strength workout for heroes')
        workout2 = Workout.objects.create(name='Speed Training', description='Speed workout for heroes')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(marvel)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
