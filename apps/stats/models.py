from django.db import models
from ..users.models import User

# Create your models here.
class StatManager(models.Model):
    pass


class Stat(models.Model):
    use_percentage = models.FloatField()
    use_points = models.FloatField()
    user_stats = models.ForeignKey(User, related_name="stats")
    Global_use = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

