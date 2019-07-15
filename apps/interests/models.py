from django.db import models
from ..users.models import User

# Create your models here.
class InterestManager(models.Model):
    pass


class Interest(models.Model):
    interest_name = models.CharField(max_length=255)
    interested_users = models.ManyToManyField(User, related_name="users_interests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

