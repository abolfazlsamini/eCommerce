from dataclasses import asdict
from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'price', 'description')

# for each product: 
class ProductSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'price', 'description', 'moreDescription', 'otherstuff')
