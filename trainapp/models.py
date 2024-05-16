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
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the description.
        """
        # Assuming 'python' as the default language for highlighting
        lexer = get_lexer_by_name('python')  # You can change this to another language if needed
        linenos = 'table'  # This can be customized based on your requirement
        options = {'title': self.name}  # Using the name of the plan as the title
        formatter = HtmlFormatter(style='friendly', linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.desc, lexer, formatter)
        super().save(*args, **kwargs)


class Trainings(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')
    date = models.DateField(blank=True)


class PlansTrainigs(models.Model):
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE,null=True)
    trainings = models.ForeignKey(Trainings, on_delete=models.CASCADE,null=True)


class Exercises(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    desc = models.TextField(blank=True, default='')


class TrainingsExercises(models.Model):
    trainings = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    series = models.IntegerField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
