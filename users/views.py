from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from .serializers import UserSerializer
from rest_framework import status


class AllUsers(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user = Users.objects.all()
        email = request.data.get("email")
        existing_user = user.filter(email=email)
        serializer = UserSerializer(data=request.data)
        if existing_user:
            return Response("user already exists", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED,)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class OneUser(APIView):
    def get(self, request, id):
        try:
            user = Users.objects.get(id=id)
            serializer = UserSerializer(user)
        except Exception:
            return Response("No Such User", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class UpdateUser(APIView):
    def put(self, request, id):
        user = Users.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    def delete(self, request, id):

        try:
            user = Users.objects.get(id=id)
            user.delete()
        except Exception:
            return Response("User not present", status=status.HTTP_404_NOT_FOUND)
        return Response("user deleted", status=status.HTTP_200_OK)
