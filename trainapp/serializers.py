from rest_framework import serializers
from .models import Plans,Plans_Trainigs,Trainings,Trainigs_Exercises,Exercises

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['id', 'name', 'desc', 'price']

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = ['id', 'name', 'desc', 'date']


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['id', 'name', 'desc', 'price']

