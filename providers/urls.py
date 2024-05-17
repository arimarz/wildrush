from django.contrib import admin
from django.urls import path
from .views import (
    ProvidersListView, ProvidersDetailView,
    ProvidersCreateView, ProvidersUpdateView, ProvidersDeleteView
)

app_name = 'providers'

urlpatterns = [
    path('', ProvidersListView.as_view(), name='provider_list'),
    path('<int:pk>/', ProvidersDetailView.as_view(), name='provider_detail'),
    path('create/', ProvidersCreateView.as_view(), name='provider_create'),
    path('<int:pk>/update/', ProvidersUpdateView.as_view(), name='provider_update'),
    path('<int:pk>/delete/', ProvidersDeleteView.as_view(), name='provider_delete'),
]