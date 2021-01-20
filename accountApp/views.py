from django.shortcuts import render


# Create your views here.
def dashboard(request):
    title = 'Dashboard'
    return render(request, 'accountApp/dashboard.html', context={'title': title})


def products(request):
    title = 'Products'
    return render(request, 'accountApp/products.html', context={'title': title})


def customer(request):
    title = 'Customer'
    return render(request, 'accountApp/customer.html', context={'title': title})


def about(request):
    title = 'About'
    return render(request, 'accountApp/about.html', context={'title': title})
