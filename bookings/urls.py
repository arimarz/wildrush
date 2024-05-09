from django.contrib import admin
from django.urls import path
from .views import (
    BookingListView, BookingDetailView,
    BookingCreateView, BookingUpdateView, BookingDeleteView
)

app_name = 'bookings'

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]