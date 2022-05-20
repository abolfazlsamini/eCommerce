from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AddToCartSerializer, ProductSerializer, ProductSerializerDetailed, UserSerializer, UpdateProfileSerializer, GetProfileSerializer
from .models import Cart, Costumer, ProductModel
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    # all product short version
class ProductViewSingleItem(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    # a single product short version
class ProductViewDetailed(ListAPIView):
    serializer_class = ProductSerializerDetailed
    queryset = ProductModel.objects.all()
    # all product Long version
class ProductViewDetailedSingleItem(RetrieveAPIView):
    serializer_class = ProductSerializerDetailed
    queryset = ProductModel.objects.all()
    # a single product Long version

@method_decorator(csrf_protect, name='dispatch')
class UpdateProfileView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer
    queryset = Costumer.objects.all()

    def patch(self, request, *args, **kwargs):
        try:
            user = self.request.user
            data = self.request.data
            phone = data['phone']
            email = data['email']
            address = data['address']
            Costumer.objects.filter(id = user.id).update(phone = phone,email = email,address=address)
            user = Costumer.objects.get(id=user.id)
            user = UpdateProfileSerializer(user)# the sheer creativity in naming veriables :)
            return Response(user.data)
        except Exception as e:
            return Response("some fields are missing! "+str(e))
    # can update phone, email and address of a user

@method_decorator(csrf_protect, name='dispatch')
class GetProfileView(ListAPIView):
    (IsAuthenticated,)
    serializer_class = GetProfileSerializer
    def get(self, request, *args, **kwargs):
            user = self.request.user      
            Costumer.objects.filter(id = user.id)
            user = Costumer.objects.get(id=user.id)
            user = UpdateProfileSerializer(user)
            return Response(user.data)
    # returns users profile fields

@method_decorator(csrf_protect, name='dispatch')
class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Costumer.objects.all()

    def create(self, request, *args, **kwargs):
        # probaboly dosent need any try/catch becouse of validated_data in serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, isCreated = Token.objects.get_or_create(user=user)
        return Response("token: " +str(token))   
    # it returnes token after every registration

@method_decorator(csrf_protect, name='dispatch')
class AddToCartView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddToCartSerializer
    queryset = Costumer.objects.all()

    def post(self, request):
        try:
            id = self.request.data
            id = id['id'] # Yes
            user = self.request.user
            cart , created= Cart.objects.get_or_create(id = user.id)
            product = ProductModel.objects.get(id=id)
            cart.items.add(product)
            return Response({"Success": (str(product) + " Was Added")})
        except Exception as e:
            return Response({"Error": str(e)})
    # it just adds a product to cart, dosen't handle remove or quantity, why? becaouse i didn't think of it

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    # permission_classes = (permissions.allowany,)
    def get(self, request, format=None):
        return Response({"SUCSSES":"CSRF Cookie set"})

@method_decorator(csrf_protect, name='dispatch')
class CustomAuthToken(ObtainAuthToken):
    pass