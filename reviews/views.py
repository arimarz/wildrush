from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import ReviewOwnerOrAdminRequiredMixin
#from django.core.exceptions import ValidationError

class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    
    def get_queryset(self):
        if self.request.user.is_provider:
            return Review.objects.filter(experience__provider=self.request.user)
        return super().get_queryset()
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['user', 'experience', 'rating', 'comment']
    template_name = 'reviews/review_create.html'
    success_url = reverse_lazy('reviews:review_list')
    def form_valid(self, form):
        form.instance.user = self.request.user  # This sets the user to the current logged-in user
        # Checks if the user has booked the experience
        if not form.instance.experience.bookings.filter(user=self.request.user).exists():
            form.add_error('experience', 'You can only review experiences you have booked.')
            return self.form_invalid(form)
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, ReviewOwnerOrAdminRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_update.html'
    success_url = reverse_lazy('reviews:review_list')

class ReviewDeleteView(LoginRequiredMixin, ReviewOwnerOrAdminRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    success_url = reverse_lazy('reviews:review_list')