from rest_framework import serializers
from product.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('url','product_name', 'description', 'price', 'image')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('product', 'user','buying_date', 'price')