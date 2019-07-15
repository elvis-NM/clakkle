from django.db import models
from ..users.models import User

# Create your models here.
class ProductManager(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    num_available = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    buyer = models.ForeignKey(User, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

