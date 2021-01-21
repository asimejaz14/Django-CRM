from django.db import models
from phone_field import PhoneField

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', null=True, unique=True)
    email = models.EmailField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name.title()


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # 1st is stored in backend, 2nd is shown at the frontend
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name.title()


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    # 1st is stored in backend, 2nd is shown at the frontend
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
