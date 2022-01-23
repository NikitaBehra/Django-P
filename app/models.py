from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = PhoneNumberField()
    email = models.EmailField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:customerList') 

class OrderDetails(models.Model):
    customer = models.ForeignKey(Customer, related_name="customer",on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_cost = models.IntegerField()
    item_quantity = models.IntegerField()
    order_choices = (
    ('pending','pending'),
    ('dispatched', 'dispatched'),
    ('delivered','delivered'),
        )
    order_status = models.CharField(max_length=30, choices=order_choices, default='pending')    
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('app:orderList')     