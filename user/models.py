from django.db import models
from django.contrib.auth.models import User

# Create your models here.\

class Bussiness(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bussiness', on_delete=models.CASCADE, default=1)
