from django.contrib import admin
from .models import ProductModel, Costumer
# Register your models here.
# this is for costumized admin shit
# class ProductAdminClass(admin.ModelAdmin):
#     list = ('name', 'price')


admin.site.register(ProductModel)
admin.site.register(Costumer)