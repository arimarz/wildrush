from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sport

class SportListView(ListView):
    model = Sport
    template_name =  'sports/sport_list.html'

class SportDetailView(DetailView):
    model = Sport
    template_name =  'sports/sport_detail.html'

class SportCreateView(CreateView):
    model = Sport
    template_name =  'sports/sport_create.html'

class SportUpdateView(UpdateView):
    model = Sport
    template_name =  'sports/sport_update.html'

class SportDeleteView(DeleteView):
    model = Sport
    template_name =  'sports/sport_delete.html'