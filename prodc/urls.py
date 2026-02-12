from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BulkProduct

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product') 
# router.register(r'bulk-products', BulkProduct, basename='bulk-product')

urlpatterns = [
    path('', include(router.urls)),
    path('bulk-products/', BulkProduct.as_view(), name='bulk-product'),
]