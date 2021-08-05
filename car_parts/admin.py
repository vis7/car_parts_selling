from django.contrib import admin
from .models import CarPart, User, Seller, Buyer, Purchase


# Register your models here.
admin.site.register(CarPart)
admin.site.register(User)

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Purchase)