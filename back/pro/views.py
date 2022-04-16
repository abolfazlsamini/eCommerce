from urllib import request
from rest_framework import viewsets
from yaml import serialize
from .serializers import ProductSerializer, ProductSerializerDetailed
from .models import ProductModel


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductViewDetailed(viewsets.ModelViewSet):
    serializer_class = ProductSerializerDetailed
    queryset = ProductModel.objects.all()
