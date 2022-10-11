# from django.core import serializers
from rest_framework import serializers
from .models import User_details,User_address,User_payment

class user_detail_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_details
        fields = '__all__'

class user_address_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_address
        fields = '__all__'

class user_payment_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_payment
        fields = '__all__'