from rest_framework import serializers
from .models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'date', 'status', 'quantity', 'productId', 'userId')

    def create(self, validated_data):

        order = Orders.objects.create(
            status=validated_data.get('status', 'pending'), productId=validated_data.get('productId', ''), quantity=validated_data.get('quantity', ''), userId=validated_data.get('userId', ''))
        order.save()
        return order
