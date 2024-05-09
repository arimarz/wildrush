from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Subscription
from django.urls import reverse_lazy

class SubscriptionCreateView(CreateView):
    model = Subscription
    fields = ['user', 'provider', 'start_date', 'end_date']  
    template_name = 'subscriptions/subscription_create.html'
    success_url = reverse_lazy('subscriptions:subscription_list')

class SubscriptionUpdateView(UpdateView):
    model = Subscription
    fields = ['user', 'provider', 'start_date', 'end_date']  
    template_name = 'subscriptions/subscription_update.html'
    success_url = reverse_lazy('subscriptions:subscription_list')

class SubscriptionDeleteView(DeleteView):
    model = Subscription
    template_name = 'subscriptions/subscription_delete.html'
    success_url = reverse_lazy('subscriptions:subscription_list')

class SubscriptionListView(ListView):
    model = Subscription
    template_name = 'subscriptions/subscription_list.html'

class SubscriptionDetailView(DetailView):
    model = Subscription
    template_name = 'subscriptions/subscription_detail.html'

