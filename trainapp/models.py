from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.
class Plans(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE, null=True)


class PlansUsers(models.Model):
    user = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plans, related_name='plans', on_delete=models.CASCADE)


class Trainings(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')
    date = models.DateField(blank=True)


class PlansTrainings(models.Model):
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE, null=True)
    trainings = models.ForeignKey(Trainings, on_delete=models.CASCADE, null=True)


class Exercises(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')


class TrainingsExercises(models.Model):
    trainings = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    series = models.IntegerField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
