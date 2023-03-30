from django.db import models
from datetime import datetime
# Create your models here.

class Menu(models.Model):
    # dishes available in the canteen
    Item_Name = models.TextField(max_length=50)
    Price = models.PositiveIntegerField(default=20)
    
class Bill(models.Model):
    # A Bill object is generated for each user each month and deleted when the month's dues are cleared
    User_Name = models.TextField(max_length=20,primary_key=True)
    Name = models.TextField(max_length=30)
    Amount = models.IntegerField(default=0)
    
class Order(models.Model):
    # An Order object is generated when an item is placed in the cart (not when a dish is ordered)
    # A set of boolean variables record whether the item is merely in the cart, has been requested
    # or if the order has been accepted and is being prepared, or has been delivered
    User_Name = models.CharField(max_length=20)
    Name = models.TextField(max_length=30)
    Item_Name = models.TextField(max_length=50,null=True,)
    Price = models.PositiveIntegerField(default=20)
    Quantity = models.PositiveIntegerField(default=1)
    Amount = models.PositiveIntegerField(default=20)
    Order_Date_Time = models.DateTimeField()
    Cart_Status = models.BooleanField(default=False)
    Processing_Status = models.BooleanField(default=False)
    Accepted_Status = models.BooleanField(default=False)
    History_Status = models.BooleanField(default=False)
    Served_Status = models.BooleanField(default=False)
    Payment_Status = models.BooleanField(default=False)