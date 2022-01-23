from django import forms

from .models import Customer, OrderDetails
  
# create a ModelForm
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'customer-input'}),
            'contact' :forms.TextInput(attrs={'class': 'customer-input'}),
            'email':forms.TextInput(attrs={'class': 'customer-input'}),
            'address':forms.TextInput(attrs={'class': 'customer-input'}),
            'city' :forms.TextInput(attrs={'class': 'customer-input'}),
            'state' :forms.TextInput(attrs={'class': 'customer-input'}),
            'date':forms.TextInput(attrs={'class': 'customer-input'}),
        }
    

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = "__all__"
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'order-input-field'}),
            'item_name' :forms.TextInput(attrs={'class': 'order-input-field'}),
            'item_cost':forms.TextInput(attrs={'class': 'order-input-field'}),
            'item_quantity':forms.TextInput(attrs={'class': 'order-input-field'}),
            'order_status': forms.TextInput(attrs={'class': 'order-input-field'})
        }        