from django.db import models

# Create your models here.

class Template(models.Model):
    name = models.CharField(max_length=256)
    struct = models.JSONField(verbose_name="structure", default='{"selling_price":"","buying_price":""}')

    def __repr__(self): return f"{self.name}"


