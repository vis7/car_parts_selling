from django.urls import path
from .views import (   
    SellerSignupView, UserDetailView, SellerListView, CarPartCreate,
    CarPartDetailView, CarPartListView
)

app_name = 'car_parts'
urlpatterns = [
    path('seller/signup/', SellerSignupView.as_view(), name='seller_signup'),
    # path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller_detail'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('seller/', SellerListView.as_view(), name='seller_list'),
    path('', CarPartListView.as_view(), name='car_part_list'),
    path('create', CarPartCreate.as_view(), name='car_part_create'),
    path('<int:pk>', CarPartDetailView.as_view(), name='car_part_detail')
]
