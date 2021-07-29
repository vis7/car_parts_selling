# from django.db import transaction
# from django.contrib.auth.forms import UserCreationForm
# from .models import Seller , User
# from django import forms
# # from django.contrib.auth.models import User


# class SellerSignupForm(UserCreationForm):
#     name = forms.CharField(max_length=32)

#     class Meta(UserCreationForm.Meta):
#         model = User
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_seller = True
#         user.save()
#         c_user = Seller.objects.create(user=user)
#         # c_user.name = self.cleaned_data.get('name')
#         print(self.cleaned_data)
#         return user

    # @transaction.atomic
    # def save(self):
    #     print('hello from save of seller signup form')
    #     user = super(SellerSignupForm, self).save(commit=False)
    #     user.is_seller = True
    #     user.save()
    #     Seller.objects.create(user=user)
    #     print('seller is created successfully')
    #     user.save()
    #     return user

    # def save(self, *args, **kwargs):
    #     print('overriding save method of form')
    #     return super().save(*args, **kwargs)

    # def form_valid(self, *args, **kwargs):
    #     print('overriding form_valid method of form')
    #     return super().save(*args, **kwargs)

