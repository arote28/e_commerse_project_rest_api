from django.contrib import admin
from .models import User_address,User_details,User_payment
# Register your models here.
admin.register(User_details)
admin.register(User_address)
admin.register(User_payment)