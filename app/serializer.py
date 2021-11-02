from rest_framework import serializers
from .models import Service, Barber, Appointment
# cloudinary
from cloudinary.models import CloudinaryField
# user
from django.contrib.auth.models import User


# get all users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'date_joined')


# create user
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# get all services
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'price', 'description')


# create service
class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'price', 'description')

    def create(self, validated_data):
        service = Service.objects.create(**validated_data)
        return service
