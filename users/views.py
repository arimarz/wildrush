from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'  
    login_url = '/login/'  

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'  

class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    template_name = 'users/user_form.html'
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    success_url = reverse_lazy('users:user_list')
    permission_required = 'users.add_user'  

class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    template_name = 'users/user_form.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('users:user_list')
    permission_required = 'users.change_user'  

class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')
    permission_required = 'users.delete_user'