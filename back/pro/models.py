from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, default=None, null=True)
    # these are for different api and page vvv
    moreDescription = models.CharField(max_length=500, default=None, null=True)
    otherstuff = models.CharField(max_length=500, default=None, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    items = models.ManyToManyField(ProductModel)


class Costumer(AbstractBaseUser):
    objects =  UserManager()
    username = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE, null=True)

