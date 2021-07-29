from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
# from .forms import SellerSignupForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.urls import reverse

# Create your views here.
class SellerSignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/seller_signup.html'
    # fields = ['first_name', 'last_name', 'username', 'email', 'password']
    
    # success_url = reverse_lazy('user_detail', kwargs={'pk':self.pk})
    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk':self.pk})
    # def get_context_data(self, **kwargs):
    #     # kwargs['user_type'] = 'cuser'
    #     return super().get_context_data(**kwargs)


class SellerDetailView(DetailView):
    model = User
    template_name = 'car_parts/user_details.html'

    def get_object(self):
        pk = self.kwargs['pk']
        return User.objects.get(pk=pk)

# User view
class UserDetailView(DetailView):
    model = User
    template_name = 'car_parts/user_details.html'

    def get_object(self):
        pk = self.kwargs['pk']
        return User.objects.get(pk=pk)
