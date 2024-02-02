from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import TrackingSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import OrderTrack
from users.models import Users
from orders.models import Orders
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.


class AddTrack(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        context = {"request": "put"}
        serializer = TrackingSerializer(data=request.data, context=context)

        if serializer.is_valid():
            serializer.save()
            d = serializer.data
            response = {}
            if d.get('confirmed'):
                response.update({'confirmed': d.get('confirmed')})
            if d.get('dispatched'):
                response.update({'dispatched': d.get('dispatched')})
            if d.get('shipped'):
                response.update({'shipped': d.get('shipped')})
            if d.get('in_transit'):
                response.update({'in_transit': d.get('in_transit')})
            if d.get('out_for_delivery'):
                response.update(
                    {'out_for_delivery': d.get('out_for_delivery')})
            if d.get('final_status'):

                response.update({'final_status': d.get('final_status')})
            if d.get('orderId'):
                response.update({'orderId': d.get('orderId')})

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchAllOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        track = OrderTrack.objects.all()
        try:
            serializer = TrackingSerializer(track, many=True)

        except OrderTrack.DoesNotExist:
            return Response("No Order found", status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        response = {}

        for d in data:
            order_id = d.get('orderId')
            order_info = {}

            if d.get('confirmed'):
                order_info.update({'confirmed': d.get('confirmed')})
            if d.get('dispatched'):
                order_info.update({'dispatched': d.get('dispatched')})
            if d.get('shipped'):
                order_info.update({'shipped': d.get('shipped')})
            if d.get('in_transit'):
                order_info.update({'in_transit': d.get('in_transit')})
            if d.get('out_for_delivery'):
                order_info.update(
                    {'out_for_delivery': d.get('out_for_delivery')})

            order_info.update({'final_status': d.get('final_status')})

            response.update({f'Order Id {order_id}': order_info})
        return Response(response, status=status.HTTP_200_OK)


class FetchOrderTrack(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        print(request)

        try:
            user = Users.objects.get(id=request.user.id)

            orders = Orders.objects.filter(userId=user)
            order = orders.get(id=id)
            track = OrderTrack.objects.filter(orderId=order.id)
            serializer = TrackingSerializer(track, many=True)
        except Orders.DoesNotExist:
            return Response("no order to track", status=status.HTTP_404_NOT_FOUND)
        data = serializer.data

        response = {}

        for d in data:
            order_id = d.get('orderId')
            order_info = {}

            if d.get('confirmed'):
                order_info.update({'confirmed': d.get('confirmed')})
            if d.get('dispatched'):
                order_info.update({'dispatched': d.get('dispatched')})
            if d.get('shipped'):
                order_info.update({'shipped': d.get('shipped')})
            if d.get('in_transit'):
                order_info.update({'in_transit': d.get('in_transit')})
            if d.get('out_for_delivery'):
                order_info.update(
                    {'out_for_delivery': d.get('out_for_delivery')})

            order_info.update({'final_status': d.get('final_status')})

            response.update({f'Order Id {order_id}': order_info})

        return Response(response, status=status.HTTP_200_OK)


class UpdateOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, id):

        try:
            track = OrderTrack.objects.get(pk=id)
        except OrderTrack.DoesNotExist:
            return Response("No order present to track", status=status.HTTP_404_NOT_FOUND)
        serializer = TrackingSerializer(track, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data

            order_info = {}
            print(data.get('confirmed'))
            print(data.get('dispatched'))
            print(data.get('shipped'))
            print(data.get('in_transit'))
            print(data.get('out_for_delivery'))
            if data.get('confirmed'):
                order_info.update({'confirmed': data.get('confirmed')})

            if data.get('dispatched'):

                order_info.update({'dispatched': data.get('dispatched')})
                print(order_info)
            if data.get('shipped'):
                order_info.update({'shipped': data.get('shipped')})
            if data.get('in_transit'):
                order_info.update({'in_transit': data.get('in_transit')})
            if data.get('out_for_delivery'):
                order_info.update(
                    {'out_for_delivery': data.get('out_for_delivery')})
            order_info.update({'final_status': data.get('final_status')})
    
            return Response(order_info, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):

        try:
            track = OrderTrack.objects.get(pk=id)
        except OrderTrack.DoesNotExist:
            return Response("No such order present", status=status.HTTP_404_NOT_FOUND)
        track.delete()
        return Response("Order Tracking deleted", status=status.HTTP_200_OK)


class DeleteAllOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request):

        try:
            track = OrderTrack.objects.all()
        except OrderTrack.DoesNotExist:
            return Response("No such order present", status=status.HTTP_404_NOT_FOUND)
        track.delete()
        return Response("All Order Tracking deleted", status=status.HTTP_200_OK)
