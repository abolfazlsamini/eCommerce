from dataclasses import asdict
from rest_framework.response import Response
from rest_framework import serializers
from .models import Costumer, ProductModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'price', 'description')

# for each product: 
class ProductSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'price', 'description', 'moreDescription', 'otherstuff')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ('id', 'username', 'password', 'email', 'address' ,'phone', 'cart')
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        
        user = User.objects.create_user(validated_data['username'],None,validated_data['password'])
        return user
            

    #     return super().create(validated_data)
    #     user.setpassword