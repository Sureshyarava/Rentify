from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializer import CustomUserSerializer, BasicUserSerializer
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView


class RegisterUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsersView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = list(CustomUser.objects.all())
        serializer = BasicUserSerializer(instance=users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None

        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username, password=password)
            except ObjectDoesNotExist:
                pass
        if not user:
            try:
                user = CustomUser.objects.get(username=username, password=password)
            except ObjectDoesNotExist:
                pass
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={"message": "User Logged in Successfully",
                                  "token": token.key}, status=status.HTTP_200_OK)
        return Response(data={"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(data={"message": "User Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
