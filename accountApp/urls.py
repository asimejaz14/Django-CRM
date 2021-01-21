
from django.urls import path
from accountApp import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),

]
