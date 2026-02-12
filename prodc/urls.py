from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BulkProduct

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product') 

urlpatterns = [
    path('', include(router.urls)),
    path('bulk-products/', BulkProduct.as_view(), name='bulk-product'),
]