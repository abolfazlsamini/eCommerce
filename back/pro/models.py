from django.db import models


# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name