from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

CATEGORY_TYPE = (
    ('E','engine'),
    ('FS','fuel system'),
    ('EX_S','exhaust system'),
    ('CS','cooling system'),
    ('LS','lubrication system'),
    ('EL_S','electrical system'),
    ('T','transmission'),
    ('C','chassis'),
)

# User = get_user_model()

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    def _str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
    

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'seller: {self.user.username}'

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'seller: {self.user.username}'

class CarPart(models.Model):
    part_name = models.CharField(max_length=32)
    car_model_name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE)
    description = models.TextField()
    is_new = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.part_name

class Purchase(models.Model):
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_part} is purchased by buyer {self.buyer}"


# Create your models here.



