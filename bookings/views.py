from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Booking
from django.urls import reverse_lazy

class BookingListView(ListView):
    model = Booking
    template_name =  'bookings/booking_list.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name =  'bookings/booking_detail.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['user', 'experience', 'booking_date', 'status']  
    template_name = 'bookings/booking_create.html'
    success_url = reverse_lazy('bookings:booking_list') 

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['user', 'experience', 'booking_date', 'status']  
    template_name = 'bookings/booking_update.html'
    success_url = reverse_lazy('bookings:booking_list')  

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'bookings/booking_delete.html'
    success_url = reverse_lazy('bookings:booking_list')