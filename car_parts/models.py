from django.db import models
from django.contrib.auth import get_user_model
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

User = get_user_model()

class CarPart(models.Model):
    part_name = models.CharField(max_length=32)
    car_model_name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE)
    description = models.TextField()
    is_new = models.BooleanField(default=False)
    seller = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.part_name

# class User(AbstractUser):
#     is_buyer = models.BooleanField(default=False)
#     is_seller = models.BooleanField(default=False)

#     def _str__(self):
#         return self.username

#     def get_absolute_url(self):
#         return reverse("user_detail", kwargs={"pk": self.pk})
    

# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'seller: {self.user.username}'

# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'seller: {self.user.username}'

# Create your models here.



