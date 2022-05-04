from urllib import request, response
from rest_framework import viewsets, mixins
from yaml import serialize
from .serializers import ProductSerializer, ProductSerializerDetailed, UserSerializer
from .models import ProductModel
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class ProductViewSingleItem(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductViewDetailed(ListAPIView):
    serializer_class = ProductSerializerDetailed
    queryset = ProductModel.objects.all()

class ProductViewDetailedSingleItem(RetrieveAPIView):
    serializer_class = ProductSerializerDetailed
    queryset = ProductModel.objects.all()


class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
