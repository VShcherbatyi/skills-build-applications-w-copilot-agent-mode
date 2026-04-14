from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Standard pushups', difficulty='Easy'),
            Workout.objects.create(name='Squats', description='Bodyweight squats', difficulty='Easy'),
            Workout.objects.create(name='Deadlift', description='Barbell deadlift', difficulty='Hard'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='Squats', duration=20, date=timezone.now())
        Activity.objects.create(user=users[2], type='Deadlift', duration=40, date=timezone.now())
        Activity.objects.create(user=users[3], type='Pushups', duration=25, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
