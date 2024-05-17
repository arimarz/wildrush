from django.contrib import admin
from django.urls import path
from .views import (
    ProviderListView, ProviderDetailView,
    ProviderCreateView, ProviderUpdateView, ProviderDeleteView
)

app_name = 'providers'

urlpatterns = [
    path('', ProviderListView.as_view(), name='provider_list'),
    path('<int:pk>/', ProviderDetailView.as_view(), name='provider_detail'),
    path('create/', ProviderCreateView.as_view(), name='provider_create'),
    path('<int:pk>/update/', ProviderUpdateView.as_view(), name='provider_update'),
    path('<int:pk>/delete/', ProviderDeleteView.as_view(), name='provider_delete'),
]