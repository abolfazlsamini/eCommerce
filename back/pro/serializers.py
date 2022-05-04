from dataclasses import asdict
from urllib import response
from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth.models import User


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
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],None)
        user.set_password(validated_data['password'])

        return user

    #     return super().create(validated_data)
    #     user.setpassword