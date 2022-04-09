from urllib import request
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import ProductModel

# Create your views here.
# class ProductView(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = ProductModel.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    # def __init__(self,  **kwargs):
    #     super(ProductView, self).__init__(**kwargs)
        
    queryset = ProductModel.objects.all()