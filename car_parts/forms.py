from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import Seller , User, CarPart, Buyer
from django import forms
# from django.contrib.auth.models import User


class SellerSignupForm(UserCreationForm):
    email = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.email = self.cleaned_data.get('email')
        user.save()
        seller = Seller.objects.create(user=user)
        seller.address = self.cleaned_data.get('address')
        seller.save()
        # print(self.cleaned_data)
        return user

class BuyerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        user.save()
        buyer = Buyer.objects.create(user=user)
        return buyer

class CarPartForm(forms.ModelForm):
    class Meta:
        model = CarPart
        fields = ['part_name', 'car_model_name', 'brand', 'category', 'description', 'is_new']
    