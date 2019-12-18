from rest_framework import serializers

from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['product_name', 'description', 'price', 'image']
