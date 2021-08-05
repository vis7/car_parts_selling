from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import Seller , User, CarPart
from django import forms
# from django.contrib.auth.models import User


class SellerSignupForm(UserCreationForm):
    address = forms.CharField(max_length=200)
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        c_user = Seller.objects.create(user=user)
        c_user.address = self.cleaned_data.get('address')
        c_user.save()
        print(self.cleaned_data)
        return user

class CarPartForm(forms.ModelForm):
    class Meta:
        model = CarPart
        fields = ['part_name', 'car_model_name', 'brand', 'category', 'description', 'is_new']