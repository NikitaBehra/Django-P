from pyexpat import model
from django.shortcuts import render
from django.views.generic import FormView, ListView, CreateView, DetailView, UpdateView, TemplateView
from app.models import Customer, OrderDetails
from .forms import CustomerForm, OrderForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from app.filters import CustomFilter, OrderFilter
from django.db.models import Sum
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
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filters'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
        return context 

class ItemList(TemplateView):
    model = OrderDetails
    template_name = "app/order_item_list.html"    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_name = self.kwargs["slug"]
        context["item_name"] = item_name
        context['list'] = OrderDetails.objects.filter(item_name= item_name)
        return context 

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer_detail'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        id = self.get_object().id
        # print("primary key: ",name)
        context['pending'] = OrderDetails.objects.filter(order_status="pending", customer = id).count()
        context['dispatched'] = OrderDetails.objects.filter(order_status="dispatched", customer = id).count()
        context['delivered'] = OrderDetails.objects.filter(order_status="delivered", customer = id).count()
        return context   


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ["name", "contact", "email", "address", "city", "state"]

class OrderDetailsView(DetailView):
    model = OrderDetails
    context_object_name = 'order'     

class UpdateOrderDetails(UpdateView):
    model = OrderDetails
    fields = ["customer", "item_name", "item_cost", "item_quantity", "order_status"] 
  
class StatisticsView(TemplateView):
    template_name = "app/statistics.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.count()
        context['orders'] = OrderDetails.objects.count()
        context['pending'] = OrderDetails.objects.filter(order_status="pending").count()
        context['dispatched'] = OrderDetails.objects.filter(order_status="dispatched").count()
        context['delivered'] = OrderDetails.objects.filter(order_status="delivered").count()
        context['sum'] = OrderDetails.objects.aggregate(Sum('item_cost'))
        return context

class PendingListView(TemplateView):
    template_name = "app/pendings.html" 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['pendingList'] = OrderDetails.objects.filter(order_status="pending")
        return context

class DeliveredListView(TemplateView):
    template_name = "app/delivered.html" 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['deliveredList'] = OrderDetails.objects.filter(order_status="delivered")
        return context

class DispatchedListView(TemplateView):
    template_name = "app/dispatched.html" 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['dispatchedList'] = OrderDetails.objects.filter(order_status="dispatched")
        return context
