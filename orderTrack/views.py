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

        serializer = TrackingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            data = serializer.data

            response_data = {}
            fields_to_include = ['confirmed', 'dispatched', 'shipped',
                                 'in_transit', 'out_for_delivery', 'final_status', 'orderId']

            for field in fields_to_include:
                if data.get(field):
                    response_data.update({field: data.get(field)})

            return Response(response_data, status=status.HTTP_201_CREATED)
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
        fields_to_include = ['confirmed', 'dispatched', 'shipped',
                             'in_transit', 'out_for_delivery', 'final_status', 'orderId']

        for d in data:
            track_data = {}
            for field in fields_to_include:
                if d.get(field):
                    track_data[field] = d.get(field)

            response[f"Tracking Id_{d.get('id')}"] = track_data

        return Response(response, status=status.HTTP_200_OK)


class FetchOrderTrack(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            user = Users.objects.get(id=request.user.id)

            orders = Orders.objects.filter(userId=user)
            order = orders.get(id=id)
            track = OrderTrack.objects.filter(orderId=order.id)
            serializer = TrackingSerializer(track, many=True)
        except Orders.DoesNotExist:
            return Response("no such order to track", status=status.HTTP_404_NOT_FOUND)
        data = serializer.data

        response = {}
        fields_to_include = ['id', 'confirmed', 'dispatched', 'shipped',
                             'in_transit', 'out_for_delivery', 'final_status', 'orderId']
        for d in data:
            response = {
                field: d.get(field) for field in fields_to_include if d.get(field)}
        if response == {}:

            return Response("order tracking not started yet", status=status.HTTP_204_NO_CONTENT)
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
            fields_to_include = ['confirmed', 'dispatched', 'shipped',
                                 'in_transit', 'out_for_delivery', 'final_status', 'orderId']
            for field in fields_to_include:
                if data.get(field):
                    order_info.update({field: data.get(field)})

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
