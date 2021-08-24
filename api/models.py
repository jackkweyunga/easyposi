from os import name
from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=256)

class Entry(models.Model):
    item = models.ForeignKey(Item, related_name="entries", verbose_name="entered item" ,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    item = models.ForeignKey(Item, related_name="sales", verbose_name="sold item" ,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Template(models.Model):
    name = models.CharField(max_length=256)
    struct = models.JSONField(verbose_name="structure", default='{}')




