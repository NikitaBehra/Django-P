from pyexpat import model
from django.shortcuts import render
from django.views.generic import FormView, ListView, CreateView, DetailView, UpdateView
from app.models import Customer, OrderDetails
from .forms import CustomerForm, OrderForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from app.filters import CustomFilter
# Create your views here.
def Home(request):
    context = {}
    context['customers'] = Customer.objects.all().order_by("date").reverse()[:15]
    context['orders'] = OrderDetails.objects.all().order_by("date").reverse()[:15]
    return render(request, 'app/home.html', context)



class CreateCustomer(FormView):
    # model = Customer
    form_class = CustomerForm
    fields = ["name", "contact", "email", "address", "city", "state"]
    success_url=reverse_lazy('customerList')
    template_name = "app/customer_create.html"  

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('app:customerList')

        return render(request,self.template_name, {'form': self.form_class})    


class CreateOrder(FormView):
    form_class = OrderForm
    fields = ["customer", "item_name", "item_cost", "item_quantity", "order_status"] 
    success_url=reverse_lazy('orderList')
    template_name = "app/order_create.html"  
 
    def post(self, request, *args, **kwargs):
        print("post")
        self.form_class = OrderForm(request.POST)
        if self.form_class.is_valid():
            self.form_class.save() 
            print("form is saved!")
            return redirect('app:orderList')

        return render(request,self.template_name, {'form': self.form_class})      

    

class CustomerList(ListView):
    model = Customer
    template_name = "app/customer_list.html"      
    context_object_name = 'customer_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filters'] = CustomFilter(self.request.GET, queryset=self.get_queryset())
        return context

class OrderList(ListView):
    model = OrderDetails
    template_name = "app/order_list.html"      
    context_object_name = 'order_list'  

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer_detail'


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ["name", "contact", "email", "address", "city", "state"]

class OrderDetailsView(DetailView):
    model = OrderDetails
    context_object_name = 'order'     

class UpdateOrderDetails(UpdateView):
    model = OrderDetails
    fields = ["customer", "item_name", "item_cost", "item_quantity", "order_status"] 
  