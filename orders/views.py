from django.shortcuts import render
from rest_framework.views import APIView
from .models import Orders
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from products.models import Products
# Create your views here.


class AllOrders(APIView):
    def get(self, request):

        orders = Orders.objects.all()
        serailizer = OrderSerializer(orders, many=True)
        if serailizer:
            return Response(serailizer.data, status=status.HTTP_200_OK)
        else:
            return Response("No Order found", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        pid = request.data.get('productId')

        product = Products.objects.get(id=pid)
        oquan = request.data.get('quantity')
        pquan = product.quantity
        if serializer.is_valid():
            if oquan > pquan:
                return Response("Product Out of Stock", status=status.HTTP_400_BAD_REQUEST)
            elif oquan <= pquan:
                product.quantity -= oquan
                product.save()
                serializer.save()
            return Response("Order Placed", status=status.HTTP_201_CREATED)


class OneOrder(APIView):
    def get(self, request, id):
        try:
            order = Orders.objects.get(id=id)
            serializer = OrderSerializer(order)
        except Orders.DoesNotExist:
            return Response("No such order present", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpadteOrder(APIView):
    def put(self, request, id):
        order = Orders.objects.get(id=id)
        pid = order.productId.pk
        product = Products.objects.get(id=pid)
        oquan = order.quantity
        st = request.data.get('status')

        serailizer = OrderSerializer(order, data=request.data, partial=True)
        if serailizer.is_valid():
            if st == 'cancled':
                product.quantity += oquan
                product.save()
                serailizer.save()
                return Response(serailizer.data, status=status.HTTP_202_ACCEPTED)
            else:
                serailizer.save()
                return Response(serailizer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("No data present to update", status=status.HTTP_400_BAD_REQUEST)


class DeleteOrder(APIView):
    def delete(self, request, id):
        try:
            order = Orders.objects.get(id=id)
        except Orders.DoesNotExist:
            return Response("Order Not found", status=status.HTTP_400_BAD_REQUEST)
        order.delete()
        return Response("Order deleted", status=status.HTTP_200_OK)
