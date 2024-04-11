from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128, blank=True, default=None)
    product_description = models.CharField(
        max_length=128, blank=True, default=None)
    product_price = models.CharField(max_length=128, blank=True, default=None)
    product_owner = models.CharField(max_length=128, blank=True, default=None)
    update_date = models.DateTimeField(auto_now=True, blank=False)
