from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Provider

class ProvidersListView(ListView):
    model = Provider
    template_name =  'providers/provider_list.html'

class ProvidersDetailView(DetailView):
    model = Provider
    template_name =  'providers/provider_detail.html'

class ProvidersCreateView(CreateView):
    model = Provider
    template_name =  'providers/provider_create.html'

class ProvidersUpdateView(UpdateView):
    model = Provider
    template_name =  'providers/provider_update.html'

class ProvidersDeleteView(DeleteView):
    model = Provider
    template_name =  'providers/provider_delete.html'