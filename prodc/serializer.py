from rest_framework import serializers
from .models import Product


class BulkProductSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        products = [Product(**item) for item in validated_data]
        return Product.objects.bulk_create(products)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        list_serializer_class = BulkProductSerializer

        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be a positive integer.")
            return value
        def validate_stock(self, value):
            if value < 0:
                raise serializers.ValidationError("Stock cannot be negative.")
            return value    

