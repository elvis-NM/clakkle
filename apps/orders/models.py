from django.db import models
from ..users.models import User
from ..products.models import Product


# Create your models here.


class ShippingManager(models.Manager):
    pass


class Shipping(models.Model):
    user = models.ForeignKey(User, related_name="shippings")
    shipped = models.BooleanField()
    date_shipped = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderManager(models.Manager):
    pass


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders")
    shipping = models.ForeignKey(Shipping, related_name="orders")
    fulfilled = models.BooleanField()
    date_fufilled = models.DateField()
    products = models.ManyToManyField(Product, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
