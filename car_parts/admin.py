from django.contrib import admin
from .models import CarPart, User, Seller, Buyer


# Register your models here.
admin.site.register(CarPart)
admin.site.register(User)

admin.site.register(Seller)
admin.site.register(Buyer)
