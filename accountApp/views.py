from django.shortcuts import render
from .models import Customer, Order
from django.db.models import Count


# Create your views here.
def dashboard(request):
    title = 'Dashboard'
    orders = Order.objects.all()
    total_orders = Order.objects.all().count()
    delivered_orders = Order.objects.filter(status='Delivered').count()
    pending_orders = Order.objects.filter(status='Pending').count()
    customers_orders = Customer.objects.all().values('name').annotate(total=Count('order')).order_by('date_created')
    context = {
        'title': title,
        'orders': orders,
        'total_orders': total_orders,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
        'customers_orders': customers_orders,
    }

    return render(request, 'accountApp/dashboard.html', context=context)


def products(request):
    title = 'Products'
    return render(request, 'accountApp/products.html', context={'title': title})


def customers(request):
    title = 'Customers'
    customers_orders = Customer.objects.all().values('name').annotate(total=Count('order')).order_by('date_created')
    context = {
        'title': title,

        'customers_orders': customers_orders,
    }
    return render(request, 'accountApp/customers.html', context=context)


def about(request):
    title = 'About'
    return render(request, 'accountApp/about.html', context={'title': title})
