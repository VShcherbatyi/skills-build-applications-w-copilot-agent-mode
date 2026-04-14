from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@test.com', name='Test', team=team)
        self.assertEqual(str(user), 'test@test.com')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Test', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test')
