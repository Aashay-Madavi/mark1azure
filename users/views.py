from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
Users = get_user_model()


class AllUsers(APIView):

    def post(self, request):
        user = Users.objects.all()

        email = request.data.get("email")
        phone_no = request.data.get("contactNo")

        existing_user = user.filter(email=email)
        existing_phone = user.filter(contactNo=phone_no)

        serializer = UserSerializer(data=request.data)
        if existing_user or existing_phone:
            return Response("user already exists", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED,)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class FetchUsers(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FetchUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = Users.objects.get(id=id)
            serializer = UserSerializer(user)
        except Users.DoesNotExist:
            return Response("No Such User", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class UpdateUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        user = Users.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):

        try:
            user = Users.objects.get(id=id)
            user.delete()
        except Users.DoesNotExist:
            return Response("User not present", status=status.HTTP_404_NOT_FOUND)
        return Response("user deleted", status=status.HTTP_200_OK)


class LoginUser(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = Users.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("No such user")
        # if not user.check_password(password):
        if not user.check_password(password):
            return Response("Wrong password", status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data.get('refresh')

            token = RefreshToken(refresh)
        
        except:
            return Response("no such user to Logout", status=status.HTTP_400_BAD_REQUEST)
        token.blacklist()
        return Response("Loged Out", status=status.HTTP_200_OK)
