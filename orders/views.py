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
        st = request.data.get('status')
        print(pid)
        if serializer.is_valid():
            serializer.save()
            try:
                if st == 'pending' or st == 'delivered':
                    products = Products.objects.get(id=pid)
                    products.quantity -= 1
                    products.save()
                else:
                    products = Products.objects.get(id=pid)
                    products.quantity += 1
                    products.save()

            except Exception:
                return Response("Product does exist", status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("not vaild data to enter", status=status.HTTP_400_BAD_REQUEST)


class OneOrder(APIView):
    def get(self, request, id):
        try:
            order = Orders.objects.get(id=id)
            serializer = OrderSerializer(order)
        except Exception:
            return Response("No such order present", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpadteOrder(APIView):
    def put(self, request, id):
        order = Orders.objects.get(id=id)
        serailizer = OrderSerializer(order, data=request.data, partial=True)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("No data present to update", status=status.HTTP_400_BAD_REQUEST)


class DeleteOrder(APIView):
    def delete(self, request, id):
        try:
            order = Orders.objects.get(id=id)
        except Exception:
            return Response("Order Not found", status=status.HTTP_400_BAD_REQUEST)
        order.delete()
        return Response("Order deleted", status=status.HTTP_200_OK)
