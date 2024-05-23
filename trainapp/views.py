from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from .models import Plans, Trainings, Exercises, PlansTrainigs, TrainingsExercises, PlansUsers
from .permissions import IsOwnerOrReadOnly
from .serializers import PlansSerializer, TrainingsSerializer, ExercisesSerializer, UserSerializer, \
    PlansTrainigsSerializer, TrainingsExercisesSerializer
from rest_framework import permissions


class PlansList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserPlansList(generics.ListAPIView):
    queryset = Plans.objects.filter(userplans__user=self.request.user)  # Filter by user from request
    serializer_class = PlansSerializer

    def get_queryset(self):
        # Alternatively, use a Django ORM filter backend for efficiency with large datasets
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(userplans__user=user)
        return queryset

class PlansDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TrainingsList(generics.ListAPIView):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer


class TrainingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer


class ExercisesList(generics.ListAPIView):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class ExercisesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class PlansTrainingList(generics.ListAPIView):
    queryset = PlansTrainigs.objects.all()
    serializer_class = PlansTrainigsSerializer


class PlansTrainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlansTrainigs.objects.all()
    serializer_class = PlansTrainigsSerializer


class TrainingsExerciseList(generics.ListAPIView):
    queryset = TrainingsExercises.objects.all()
    serializer_class = TrainingsExercisesSerializer


class TrainingsExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingsExercises.objects.all()
    serializer_class = TrainingsExercisesSerializer
