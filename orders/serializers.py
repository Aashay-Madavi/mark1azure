from rest_framework import serializers
from .models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('productId', 'userId', 'date', 'status')
