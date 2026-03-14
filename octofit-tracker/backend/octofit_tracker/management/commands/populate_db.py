from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_active=True)
        User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_active=True)
        User.objects.create(email='thor@marvel.com', name='Thor', team='marvel', is_active=True)
        User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_active=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_active=True)
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_active=True)

        # Create activities
        Activity.objects.create(user='Iron Man', activity_type='run', duration=30, date='2026-03-14')
        Activity.objects.create(user='Captain America', activity_type='cycle', duration=45, date='2026-03-14')
        Activity.objects.create(user='Thor', activity_type='swim', duration=25, date='2026-03-14')
        Activity.objects.create(user='Superman', activity_type='fly', duration=60, date='2026-03-14')
        Activity.objects.create(user='Batman', activity_type='train', duration=40, date='2026-03-14')
        Activity.objects.create(user='Wonder Woman', activity_type='fight', duration=35, date='2026-03-14')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=120)
        Leaderboard.objects.create(team='dc', points=110)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
