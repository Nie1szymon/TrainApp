from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Plans, Trainings, Exercises, PlansTrainings, TrainingsExercises, PlansUsers
from .serializers import PlansSerializer, TrainingsSerializer, ExercisesSerializer, UserSerializer, \
    PlansTrainigsSerializer, TrainingsExercisesSerializer, PlansUsersSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


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


class UserOwnedPlansView(generics.ListAPIView):
    serializer_class = PlansSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Plans.objects.filter(owner=user)


class UserPlansView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            plans_users = PlansUsers.objects.filter(user=user)
            plans = [pu.plan for pu in plans_users]
            serializer = PlansSerializer(plans, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = PlansUsersSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    queryset = PlansTrainings.objects.all()
    serializer_class = PlansTrainigsSerializer


class PlansTrainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlansTrainings.objects.all()
    serializer_class = PlansTrainigsSerializer


class TrainingsExerciseList(generics.ListAPIView):
    queryset = TrainingsExercises.objects.all()
    serializer_class = TrainingsExercisesSerializer


class TrainingsExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingsExercises.objects.all()
    serializer_class = TrainingsExercisesSerializer


class PlanExtTrainings(APIView):
    def get(self, request, plan_id, *args, **kwargs):
        try:
            plan = Plans.objects.get(pk=plan_id)
            plans_trainings = PlansTrainings.objects.filter(plans=plan)
            trainings = [pt.trainings for pt in plans_trainings]
            serializer = TrainingsSerializer(trainings, many=True)
            return Response(serializer.data)
        except Plans.DoesNotExist:
            return Response({'error': 'Plan not found'}, status=404)

class TrainingExtExercises(APIView):
    def get(self, request, training_id, *args, **kwargs):
        exercises = TrainingsExercises.objects.filter(trainings_id=training_id)
        serializer = TrainingsExercisesSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request, training_id, *args, **kwargs):
        data = request.data
        data['trainings'] = training_id
        serializer = TrainingsExercisesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)