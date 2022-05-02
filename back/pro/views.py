from urllib import request, response
from rest_framework import viewsets, mixins
from .serializers import ProductSerializer, ProductSerializerDetailed
from .models import ProductModel
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView


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
