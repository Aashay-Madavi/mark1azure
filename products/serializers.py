from .models import Products
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'category', 'price', 'quantity')
