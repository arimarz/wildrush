from django.contrib import admin
from django.urls import path
from .views import (
    CalendarEventListView, CalendarEventDetailView,
    CalendarEventCreateView, CalendarEventUpdateView, CalendarEventDeleteView
)

app_name = 'calendarevents'

urlpatterns = [
    path('', CalendarEventListView.as_view(), name='calendarevent_list'),
    path('<int:pk>/', CalendarEventDetailView.as_view(), name='calendarevent_detail'),
    path('create/', CalendarEventCreateView.as_view(), name='calendarevent_create'),
    path('<int:pk>/update/', CalendarEventUpdateView.as_view(), name='calendarevent_update'),
    path('<int:pk>/delete/', CalendarEventDeleteView.as_view(), name='calendarevent_delete'),
]
