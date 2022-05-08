from rest_framework.response import Response
from yaml import serialize
from .serializers import ProductSerializer, ProductSerializerDetailed, UserSerializer
from .models import ProductModel
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

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
    
    def create(self, request, *args, **kwargs):# i totally just copies most of this shit
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            token, created = Token.objects.get_or_create(user=serializer.instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            if str(e) == "UNIQUE constraint failed: auth_user.username":
                return Response("Username already exist")
            if "code='blank'" in str(e): 
                return Response("Username or password can't be empty")
            return Response(str(e))
            
#    permission_classes = (IsAuthenticated,)