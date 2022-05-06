from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pro import views
from rest_framework.authtoken.views import obtain_auth_token

# router = routers.DefaultRouter()
# router.register(r'products',views.ProductView, 'products')
# router.register(r'product',views.ProductViewDetailed, 'detailed')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-fetch', obtain_auth_token),# our login too i guess

    path('api/product/',  views.ProductView.as_view()), # short version of product for main page
    path('api/product/<pk>/',  views.ProductViewSingleItem.as_view()),# short version of a single product for idk f u
    path('api/fullproduct/',  views.ProductViewDetailed.as_view()),# long version of all products
    path('api/fullproduct/<pk>/',  views.ProductViewDetailedSingleItem.as_view()),# long version of a single product

    path('api/users/',  views.UserView.as_view()),
]

