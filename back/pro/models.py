from pyexpat import model
from django.db import models


# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, default=None, null=True)
    # just added these...
    moreDescription = models.CharField(max_length=500, default=None, null=True)
    otherstuff = models.CharField(max_length=500, default=None, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    items = models.ManyToManyField(ProductModel)

    # def __str__(self):
    #     return self.items.id