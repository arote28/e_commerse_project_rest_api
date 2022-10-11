from django.shortcuts import render,get_object_or_404,get_list_or_404,HttpResponse,Http404
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User_details,User_address,User_payment
from .serializers import User_details,User_address,User_payment
# Create your views here.

