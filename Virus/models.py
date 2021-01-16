from django.db import models

# Create your models here.
class files(models.Model):
    f_name = models.CharField(max_length=150)
    file = models.FileField()
class SuperUser(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    Photo = models.ImageField(upload_to='Super_users')
class cart(models.Model):
    User = models.CharField(max_length=150)
    product = models.CharField(max_length=150)
