from django.contrib import admin
from .models import Plans,Trainings,Exercises, Plans_Trainigs, Trainigs_Exercises
# Register your models here.
admin.site.register(Plans)
admin.site.register(Trainings)
admin.site.register(Exercises)
admin.site.register(Plans_Trainigs)
admin.site.register(Trainigs_Exercises)