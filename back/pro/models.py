from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, default=None, blank=True)
    # these are for different api and page vvv
    moreDescription = models.CharField(max_length=500, default=None, blank=True)
    otherstuff = models.CharField(max_length=500, default=None, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    items = models.ManyToManyField(ProductModel, related_name="item")
    # something = models.ForeignKey(ProductModel,on_delete=models.CASCADE, blank=True, related_name="smt")


class Costumer(AbstractUser):

    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE, blank=True)

