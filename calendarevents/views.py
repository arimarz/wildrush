from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CalendarEvent
from django.urls import reverse_lazy

class CalendarEventCreateView(CreateView):
    model = CalendarEvent
    fields = ['user', 'experience', 'event_date']  
    template_name = 'calendarevents/calendarevent_create.html'
    success_url = reverse_lazy('calendarevents:calendarevent_list')

class CalendarEventUpdateView(UpdateView):
    model = CalendarEvent
    fields = ['user', 'experience', 'event_date']  
    template_name = 'calendarevents/calendarevent_update.html'
    success_url = reverse_lazy('calendarevents:calendarevent_list')

class CalendarEventDeleteView(DeleteView):
    model = CalendarEvent
    template_name = 'calendarevents/calendarevent_delete.html'
    success_url = reverse_lazy('calendarevents:calendarevent_list')

class CalendarEventListView(ListView):
    model = CalendarEvent
    template_name =  'calendarevents/calendarevent_list.html'

class CalendarEventDetailView(DetailView):
    model = CalendarEvent
    template_name =  'calendarevents/calendarevent_detail.html'