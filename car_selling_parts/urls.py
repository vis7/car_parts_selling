"""car_selling_parts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from car_parts.views import (
    SellerSignupView, UserDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seller/signup/', SellerSignupView.as_view(), name='seller_signup'),
    # path('car_parts/', include('car_parts.urls'))
    # path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller_detail'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail')
]