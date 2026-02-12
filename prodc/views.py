from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework import filters
from rest_framework.response import Response
from django.db import models
from rest_framework.decorators import action
from rest_framework import generics
from django.core.cache import cache

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']


    @action(detail=False, methods=['get'])
    def analytics(self, request):
        category = request.query_params.get('category', None)
        min_price = request.query_params.get('min_price', None)
        max_price = request.query_params.get('max_price', None)

        if category:
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)    
            
        total_products = products.count()
        total_stock = products.aggregate(total_stock=models.Sum('stock'))['total_stock']
        average_price = products.aggregate(average_price=models.Avg('price'))['average_price']

        data = {
            'total_products': total_products,
            'total_stock': total_stock,
            'average_price': average_price,
        }
        return Response(data)
    
class BulkProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['category', 'price']

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data, many=True) 
            serializer.is_valid(raise_exception=True)

            cache_key = 'bulk_product_cache'
            cache.set(cache_key, serializer.validated_data, timeout=5*60)
            
            return Response(serializer.data, status=201)
        except Exception as e:  
            return Response({'error': str(e)}, status=400)




