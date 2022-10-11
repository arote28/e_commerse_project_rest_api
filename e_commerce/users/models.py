from django.db import models
# import datetime
from django.utils import timezone
# Create your models here.
class User_details(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_nsme = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=200,unique=True)
    cretaed_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()

    def __str__(self):
        return self.username


class User_address(models.Model):
    user_id = models.ForeignKey(User_details,on_delete=models.CASCADE,related_name='user_adr')
    address_line1 = models.TextField(max_length=250)
    address_line2 = models.TextField(max_length=250)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    country = models.CharField(max_length=200)
    telephone = models.IntegerField()

class User_payment(models.Model):
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE, related_name='user_pay')
    payment_type = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    account_number = models.IntegerField()
    expiry_date = models.DateField()