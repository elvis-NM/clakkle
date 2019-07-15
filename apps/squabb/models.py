from django.db import models
from ..users.models import User

# Create your models here.
class SquabManager(models.Model):
    pass


class Squabb(models.Model):
    voicefile = models.FileField()
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="squabbs")
    users_liked = models.ManyToManyField(User, related_name="liked_squabbs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

