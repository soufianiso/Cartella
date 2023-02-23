from django.db import models

# Create your models here.
from django.db import models
from products.models import *
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=123, null=True)
    firstname = models.CharField(max_length=1233, null=True)
    email = models.CharField(max_length=1234, null=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    session_id = models.CharField(max_length=1235)
    date_ordered = models.DateTimeField(auto_now_add=True)
    compeleted = models.BooleanField(default=False, blank=False) 

    def __str__(self):
        return self.session_id

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    quantity = models.IntegerField() 
    
    def __str__(self):
        return str(self.product)
class ShippingInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL,  null=True, blank=True)
    address = models.CharField(max_length=12343, null=True)
    city= models.CharField(max_length=123, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address






