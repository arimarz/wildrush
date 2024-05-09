from django.contrib import admin
from django.urls import path
from .views import (
    ExperienceListView, ExperienceDetailView,
    ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView
)

app_name = 'experiences'

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    path('create/', ExperienceCreateView.as_view(), name='experience_create'),
    path('<int:pk>/update/', ExperienceUpdateView.as_view(), name='experience_update'),
    path('<int:pk>/delete/', ExperienceDeleteView.as_view(), name='experience_delete'),
]