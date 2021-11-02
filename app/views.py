from django.shortcuts import render

from app.permissions import IsAdminOrReadOnly
# from .models import Profile, Subject, Notes
from django.contrib.auth.models import User

# authentication
from django.contrib.auth import authenticate, login, logout


# api
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer,UserCreateSerializer
from .permissions import IsAdminOrReadOnly

def index(request):
    return render(request, 'index.html')



# rest api ====================================

class UserList(APIView): # list all users
    """
    List all users.
    """
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreate(APIView): # create user
    """
    Create a user.
    """
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# login user ====================================
class loginUser(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# logout user ====================================
class logoutUser(APIView): # logout user
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)
