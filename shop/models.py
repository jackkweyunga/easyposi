from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    owner = models.ForeignKey(User, related_name="shops", verbose_name="owner", on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, blank=True, default='')

    def __repr__(self): return f"{self.owner} {self.name}"

class Item(models.Model):
    name = models.CharField(max_length=256)
    shop = models.ForeignKey(Shop, related_name="items", verbose_name="shop", on_delete=models.CASCADE, default=1)
    details = models.JSONField(verbose_name="details", default='{}')
    barcode = models.CharField(max_length=256, null=True, blank=True)
    qrcode = models.CharField(max_length=256, null=True, blank=True)

    def __repr__(self): return f"{self.name}-{self.barcode}"

class Entry(models.Model):
    item = models.ForeignKey(Item, related_name="entries", verbose_name="entered item" ,on_delete=models.CASCADE, default=1)
    count = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __repr__(self): return f"{self.item.name}"

class Sale(models.Model):
    item = models.ForeignKey(Item, related_name="sales", verbose_name="sold item" ,on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=0.0)
    count = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __repr__(self): return f"{self.item.name}"










