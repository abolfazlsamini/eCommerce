import pkg_resources
from rest_framework.response import Response
from yaml import serialize
from .serializers import ProductSerializer, ProductSerializerDetailed, UpdateProfileSerializer, UserSerializer
from .models import Costumer, ProductModel
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model 

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
    queryset = Costumer.objects.all()

    def create(self, request, *args, **kwargs):
        # it returnes token after every registration
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, isCreated = Token.objects.get_or_create(user=user)
        return Response("token: " +str(token))
        # probaboly dosent need any try/catch becouse of validated_data in serializer 


class UpdateProfileView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer
    queryset = Costumer.objects.all()