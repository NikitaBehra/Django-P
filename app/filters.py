import django_filters

from . import models

class CustomFilter(django_filters.FilterSet):
    class Meta:
        model = models.Customer
        fields ={
            'name' : ["icontains"],
            'city' : ["icontains"],
        }
