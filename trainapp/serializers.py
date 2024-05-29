from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Plans, PlansTrainings, Trainings, Exercises, TrainingsExercises, PlansUsers


class PlansSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Plans
        fields = ['id', 'name', 'desc', 'price', 'owner']


class PlansUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlansUsers
        fields = ['plan']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    plans = serializers.PrimaryKeyRelatedField(many=True, queryset=Plans.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'plans']


class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = ['id', 'name', 'desc', 'date']


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['id', 'name', 'desc']


class PlansTrainigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlansTrainings
        fields = ['plans', 'trainings']


class TrainingsExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingsExercises
        fields = ['trainings', 'exercises', 'series', 'repeat']
