from django.contrib import admin
from django.urls import path
from .views import (
    SubscriptionListView, SubscriptionDetailView,
    SubscriptionCreateView, SubscriptionUpdateView, SubscriptionDeleteView
)

app_name = 'subscriptions'

urlpatterns = [
    path('', SubscriptionListView.as_view(), name='subscription_list'),
    path('<int:pk>/', SubscriptionDetailView.as_view(), name='subscription_detail'),
    path('create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('<int:pk>/update/', SubscriptionUpdateView.as_view(), name='subscription_update'),
    path('<int:pk>/delete/', SubscriptionDeleteView.as_view(), name='subscription_delete'),
]