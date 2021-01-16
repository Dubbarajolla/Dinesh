"""Bigg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import log, register, VS
from .views import redmi, Note, Nrzo, logout, diwali, ele, index, profile, more, otp, video, forgotpass, Ecom, img, qr,EcommerceList

urlpatterns = [
    path('admin', admin.site.urls),
    path('login', log),
    path('register', register),
    path('home', VS),
    path('redmi', redmi),
    path('Narzo', Nrzo),
    path('Note20', Note),
    path('logout', logout),
    path('diwali', diwali),
    path('electronic.html',ele),
    path('', index),
    path('profile', profile),
    path('more',more),
    path('otp', otp),
    path('video', video),
    path('forgotpass', forgotpass),
    path('ecom', Ecom),
    path('pic', img),
    path('qr', qr),
    path('Ecommerce', EcommerceList.as_view())

]
