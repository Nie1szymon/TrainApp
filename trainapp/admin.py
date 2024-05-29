from django.contrib import admin
from .models import Plans,Trainings,Exercises, PlansTrainings, TrainingsExercises, PlansUsers
# Register your models here.
admin.site.register(Plans)
admin.site.register(Trainings)
admin.site.register(Exercises)
admin.site.register(PlansTrainings)
admin.site.register(TrainingsExercises)
admin.site.register(PlansUsers)