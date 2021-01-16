from django.db import models
from django.contrib import admin


# Create your models here.

class Ecommerce(models.Model):
    Brand = models.CharField(max_length=100)
    Name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.FileField(upload_to='pictures')
    features = models.TextField()
    mobile_no = models.CharField(max_length=100)

class my_image(models.Model):
    image = models.ImageField(upload_to='Photos')
    Name = models.CharField(max_length=150)












