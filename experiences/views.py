from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Experience
from django.urls import reverse_lazy

class ExperienceCreateView(CreateView):
    model = Experience
    fields = ['sport', 'provider', 'price', 'duration', 'capacity']  
    template_name = 'experiences/experience_create.html'
    success_url = reverse_lazy('experiences:experience_list')

class ExperienceUpdateView(UpdateView):
    model = Experience
    fields = ['sport', 'provider', 'price', 'duration', 'capacity'] 
    template_name = 'experiences/experience_update.html'
    success_url = reverse_lazy('experiences:experience_list')

class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = 'experiences/experience_delete.html'
    success_url = reverse_lazy('experiences:experience_list')

class ExperienceListView(ListView):
    model = Experience
    template_name =  'experiences/experience_list.html'

class ExperienceDetailView(DetailView):
    model = Experience
    template_name =  'experiences/experience_detail.html'

