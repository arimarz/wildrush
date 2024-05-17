from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Experience
from django.urls import reverse_lazy
from users.mixins import ProviderRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ExperienceCreateView(LoginRequiredMixin, ProviderRequiredMixin, CreateView):
    model = Experience
    fields = ['sport', 'price', 'duration', 'capacity']  # Remove 'provider' since it will be set automatically
    template_name = 'experiences/experience_create.html'
    success_url = reverse_lazy('experiences:experience_list')

    def form_valid(self, form):
        form.instance.provider = self.request.user.provider_profile
        return super().form_valid(form)

class ExperienceUpdateView(LoginRequiredMixin, ProviderRequiredMixin, UpdateView):
    model = Experience
    fields = ['sport', 'price', 'duration', 'capacity']  # Remove 'provider' since it should not be changed
    template_name = 'experiences/experience_update.html'
    success_url = reverse_lazy('experiences:experience_list')

    def get_queryset(self):
        # Providers can only update their own experiences
        return Experience.objects.filter(provider=self.request.user.provider_profile)

class ExperienceDeleteView(LoginRequiredMixin, ProviderRequiredMixin, DeleteView):
    model = Experience
    template_name = 'experiences/experience_delete.html'
    success_url = reverse_lazy('experiences:experience_list')

    def get_queryset(self):
        # Providers can only delete their own experiences
        return Experience.objects.filter(provider=self.request.user.provider_profile)

class ExperienceListView(ListView):
    model = Experience
    template_name = 'experiences/experience_list.html'

class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'experiences/experience_detail.html'

class ProviderOnlyExperienceView(LoginRequiredMixin, ProviderRequiredMixin, ListView):
    model = Experience
    template_name = 'experiences/provider_experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        # Providers can only see their own experiences in this view
        return Experience.objects.filter(provider=self.request.user.provider_profile)

