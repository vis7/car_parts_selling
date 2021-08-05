from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import SellerSignupForm, CarPartForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.urls import reverse
from .models import Seller, CarPart

# Create your views here.
class SellerSignupView(CreateView):
    model = User
    form_class = SellerSignupForm
    template_name = 'registration/seller_signup.html'
    # fields = ['first_name', 'last_name', 'username', 'email', 'password']
    
    # success_url = reverse_lazy('user_detail', kwargs={'pk':self.pk})
    def get_success_url(self):
        return reverse('seller_list')
    # def get_context_data(self, **kwargs):
    #     # kwargs['user_type'] = 'cuser'
    #     return super().get_context_data(**kwargs)


class SellerDetailView(DetailView):
    model = User
    template_name = 'car_parts/user_details.html'

    def get_object(self):
        pk = self.kwargs['pk']
        return User.objects.get(pk=pk)

class SellerListView(ListView):
    model = Seller
    template_name = 'car_parts/seller_list.html'
    queryset = Seller.objects.all()

# User view
class UserDetailView(DetailView):
    model = User
    template_name = 'car_parts/user_details.html'

    def get_object(self):
        pk = self.kwargs['pk']
        return User.objects.get(pk=pk)

def index_view(request):
    return render(request, 'car_parts/index.html')

class CarPartCreate(CreateView):
    model = CarPart
    form_class = CarPartForm
    template_name = 'car_parts/car_part_create.html'

    def get_success_url(self):
        return redirect(reverse('car_parts_detail', kwargs={'pk':self.pk}))
    
    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)

class CarPartDetailView(DetailView):
    model = CarPart
    template_name = 'car_parts/car_part_detail.html'

    def get_object(self):
        return get_object_or_404(CarPart, pk=self.kwargs['pk'])