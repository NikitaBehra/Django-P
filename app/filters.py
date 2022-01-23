import django_filters

from . import models

class CustomFilter(django_filters.FilterSet):
    class Meta:
        model = models.Customer
        fields ={
            'name' : ["icontains"],
            'city' : ["icontains"],
        }

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = models.OrderDetails
        fields = ['item_name', 'order_status']