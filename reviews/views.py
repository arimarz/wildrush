from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from django.urls import reverse_lazy

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    fields = ['user', 'experience', 'rating', 'comment']
    template_name = 'reviews/review_create.html'
    success_url = reverse_lazy('reviews:review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['rating', 'comment'] 
    template_name = 'reviews/review_update.html'
    success_url = reverse_lazy('reviews:review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    success_url = reverse_lazy('reviews:review_list')