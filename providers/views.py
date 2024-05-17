from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .models import Provider
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ProviderRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_provider

class ProviderCreateView(LoginRequiredMixin, ProviderRequiredMixin, CreateView):
    model = Provider
    fields = ['name', 'location', 'contact_info']
    template_name = 'providers/provider_form.html'
    success_url = reverse_lazy('providers:provider_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProviderUpdateView(LoginRequiredMixin, ProviderRequiredMixin, UpdateView):
    model = Provider
    fields = ['name', 'location', 'contact_info']
    template_name = 'providers/provider_form.html'
    success_url = reverse_lazy('providers:provider_list')

    def get_object(self):
        return self.request.user.provider_profile

class ProviderDetailView(LoginRequiredMixin, ProviderRequiredMixin, DetailView):
    model = Provider
    template_name = 'providers/provider_detail.html'

    def get_object(self):
        return self.request.user.provider_profile

class ProviderDeleteView(LoginRequiredMixin, ProviderRequiredMixin, DeleteView):
    model = Provider
    template_name = 'providers/provider_confirm_delete.html'
    success_url = reverse_lazy('providers:provider_list')

    def get_object(self):
        return self.request.user.provider_profile

class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'providers/provider_list.html'
    context_object_name = 'providers'