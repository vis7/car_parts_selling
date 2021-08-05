from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import SellerSignupForm, CarPartForm, BuyerSignupForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.urls import reverse
from .models import Seller, CarPart, Purchase, Buyer
from django.views.generic.base import View
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class SellerSignupView(CreateView):
    model = User
    form_class = SellerSignupForm
    template_name = 'registration/seller_signup.html'
    
    # success_url = reverse_lazy('user_detail', kwargs={'pk':self.pk})
    def get_success_url(self):
        return reverse('car_parts:seller_list')

class BuyerSignupView(CreateView):
    model = Buyer
    form_class = BuyerSignupForm
    template_name = 'registration/seller_signup.html'

    def get_success_url(self):
        return reverse('car_parts:car_part_list')


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

    # def get_success_url(self):
    #     return redirect(reverse('car_parts_detail', kwargs={'pk':self.pk}))
    
    def post(self, request, *args, **kwargs):
        form = CarPartForm(request.POST or None)
        if form.is_valid():
            car_part = form.save(commit=False)
            car_part.seller = request.user.seller
            car_part.save()
        return redirect(reverse('car_parts:car_part_list'))

class CarPartDetailView(DetailView):
    model = CarPart
    template_name = 'car_parts/car_part_detail.html'

    def get_object(self):
        return get_object_or_404(CarPart, pk=self.kwargs['pk'])

class CarPartListView(ListView):
    model = CarPart
    template_name='car_parts/car_part_list.html'

    def get_queryset(self):
        # return super().get_queryset()
        return CarPart.objects.filter(category='E')
    
    def post(self, request):
        category_name = request.POST.get('category_name', None)
        car_parts = CarPart.objects.filter(category=category_name)
        context = {
            "carpart_list": car_parts
        }
        return render(request, self.template_name, context)

class CarPartPurchaseView(View):
    def post(self, request, *args, **kwargs):
        # add entry in purchase
        car_part_pk = kwargs.get('pk')
        car_part = CarPart.objects.get(pk=car_part_pk)
        po = Purchase.objects.create(car_part=car_part, buyer=request.user.buyer)
        
        # send mail to seller
        subject= ' it  means a world to us '
        message = f'congretulations {car_part.seller.user.username} your part {car_part.part_name} is purchased by {request.user}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [ car_part.seller.user.email ]
        send_mail( subject, message, email_from, recipient_list )  

        if po:
            msg = "Purchase successfully."
        else:
            msg = "Not Purchased. Try again."
        context = {
            'msg':msg
        }
        return render(request, 'car_parts/purchase.html', context)

    # def get(self, request, *args, **kwargs):
    #     return