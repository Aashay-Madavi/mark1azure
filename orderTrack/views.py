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
        try:
            serializer.is_valid()
            serializer.save()
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FetchAllOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        track = OrderTrack.objects.all()
        try:
            serializer = TrackingSerializer(track, many=True)

        except OrderTrack.DoesNotExist:
            return Response("No Order found", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
            return Response("no order to track", status=status.HTTP_404_NOT_FOUND)
        data = serializer.data
        response = []
        for d in data:
            if d.get('confirmed') == True:
                response.append("confirmed")
            if d.get('dispatched') == True:
                response.append("dispatched")
            if d.get('shipped') == True:
                response.append("shipped")
            if d.get('in_transit') == True:
                response.append("in_transit")
            if d.get('out_for_delivered') == True:
                response.append("out_for_delivery")
            response.append(d.get('final_status'))

        return Response(response, status=status.HTTP_200_OK)


class UpdateOrderTrack(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, id):
        try:
            track = OrderTrack.objects.get(pk=id)
        except OrderTrack.DoesNotExist:
            return Response("No such order present", status=status.HTTP_404_NOT_FOUND)
        serializer = TrackingSerializer(track, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
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
        return Response("Order deleted", status=status.HTTP_200_OK)
