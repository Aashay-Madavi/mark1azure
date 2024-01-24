from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Products
from django.http import Http404

# Create your views here.


class AllProducts(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        product = Products.objects.all()
        name = request.data.get("name")
        existing_product = product.filter(name=name)
        if existing_product:
            return Response({'error': "already existing"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneProduct(APIView):
    def get(self, request, pk):
        try:
            products = get_object_or_404(Products, pk=pk)
            serializer = ProductSerializer(products)
        except Http404:

            return Response("No such product")
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProduct(APIView):
    def put(self, request, pk):
        product = Products.objects.get(pk=pk)
        serializer = ProductSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(APIView):
    def delete(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
            product.delete()
            return Response("Record deleted", status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response("No Such Product ", status=status.HTTP_404_NOT_FOUND)
