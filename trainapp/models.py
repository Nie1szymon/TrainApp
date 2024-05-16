from django.db import models

# Create your models here.
class Plans(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

class Trainings(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')
    date = models.DateField(blank=True)

class Plans_Trainigs(models.Model):
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE),
    trainigs = models.ForeignKey(Trainings, on_delete=models.CASCADE),


class Exercises(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')

class Trainigs_Exercises(models.Model):
    trainigs = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    series = models.IntegerField(blank=True,null=True)
    repeat = models.IntegerField(blank=True,null=True)

