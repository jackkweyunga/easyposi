from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    owner = models.ForeignKey(User, related_name="shops", verbose_name="owner", on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, blank=True, default='')
    details = models.JSONField(verbose_name="details", default=dict)

    def __str__(self): return f"{self.owner} {self.name}"

class Item(models.Model):
    name = models.CharField(max_length=256)
    shop = models.ForeignKey(Shop, related_name="items", verbose_name="shop", on_delete=models.CASCADE, default=1)
    details = models.JSONField(verbose_name="details", default=dict)
    buying_price = models.FloatField(default=0.0)
    selling_price = models.FloatField(default=0.0)
    barcode = models.CharField(max_length=256, null=True, blank=True)
    qrcode = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self): return f"{self.name}-{self.barcode}"

class Entry(models.Model):
    item = models.ForeignKey(Item, related_name="entries", verbose_name="entered item" ,on_delete=models.CASCADE, default=1)
    count = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(verbose_name="details", default=dict)

    def __str__(self): return f"{self.item.name}"


def discount(initial_price, final_price):
    if final_price < initial_price:
        disc = initial_price - final_price
        return disc

def profit(buying_price, selling_price):
    if buying_price < selling_price:
        profit = selling_price - buying_price
        return profit

def loss(buying_price, selling_price):
    if buying_price > selling_price:
        loss = buying_price - selling_price
        return loss


class Sale(models.Model):
    item = models.ForeignKey(Item, related_name="sales", verbose_name="sold item" ,on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=0.0)
    count = models.IntegerField(default=1)
    discount = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    loss = models.FloatField(default=0.0)
    details = models.JSONField(verbose_name="details", default=dict)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.item.name}"

    def save(self, *args, **kwargs):
        # do_something()
        entry = Entry.objects.get(item = self.item)
        if entry.count == 0:
            pass
        elif entry.count > 0 and entry.count >= self.count:
            entry.count -= self.count
            entry.save()

            # profit
            if profit(self.item.buying_price, self.price):
                self.profit = profit(self.item.buying_price, self.price)

            # loss
            if loss(self.item.buying_price, self.price):
                self.loss = loss(self.item.buying_price, self.price)

            # profit
            if discount(self.item.selling_price, self.price):
                self.discount = discount(self.item.selling_price, self.price)

            super().save(*args, **kwargs)  # Call the "real" save() method.
        else: pass










