from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from trainapp import views

urlpatterns = [
    path('plans/', views.PlansList.as_view(), name='plans_list'),
    path('plans/<int:pk>/', views.PlansDetail.as_view(), name='plans_detail'),
    path('trainings/', views.TrainingsList.as_view(), name='trainings_list'),
    path('trainings/<int:pk>/', views.TrainingsDetail.as_view(), name='trainings_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
