from django.contrib import admin
from .models import Plans,Trainings,Exercises, PlansTrainigs, TrainingsExercises
# Register your models here.
admin.site.register(Plans)
admin.site.register(Trainings)
admin.site.register(Exercises)
admin.site.register(PlansTrainigs)
admin.site.register(TrainingsExercises)