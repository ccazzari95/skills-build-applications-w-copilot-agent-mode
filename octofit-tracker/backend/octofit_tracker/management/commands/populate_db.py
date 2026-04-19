from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2024, 1, 1))
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date(2024, 1, 2))
        Activity.objects.create(user=users[2], type='swim', duration=60, date=date(2024, 1, 3))
        Activity.objects.create(user=users[3], type='yoga', duration=20, date=date(2024, 1, 4))

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], points=100, rank=1)
        Leaderboard.objects.create(user=users[1], points=90, rank=2)
        Leaderboard.objects.create(user=users[2], points=80, rank=3)
        Leaderboard.objects.create(user=users[3], points=70, rank=4)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
