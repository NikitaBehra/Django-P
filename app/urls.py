from django.conf.urls import url

from app import views
from app.views import CreateCustomer, CreateOrder, CustomerList, OrderList, CustomerDetailView, UpdateCustomer, OrderDetailsView, UpdateOrderDetails
app_name = "app"
urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^createCustomer/', CreateCustomer.as_view(), name='createCustomer'),
    url(r'^createOrder/', CreateOrder.as_view(), name='createOrder'),
    url(r'^customerList/', CustomerList.as_view(), name='customerList'),
    url(r'^customerDetails/(?P<pk>\d+)/$',CustomerDetailView.as_view(), name="customerDetails"),
    url(r'^customerDetails/(?P<pk>\d+)/$',CustomerDetailView.as_view(), name="customerDetails"),
    url(r'^orderList/', OrderList.as_view(), name='orderList'),
    url(r'^updateCustomer/(?P<pk>\d+)/', UpdateCustomer.as_view(), name='updateCustomer'),
    url(r'^orderDetails/(?P<pk>\d+)/', OrderDetailsView.as_view(), name='orderDetails'),
    url(r'^updateOrder/(?P<pk>\d+)/', UpdateOrderDetails.as_view(), name='updateOrder'),
]
