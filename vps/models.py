from django.db import models
from domain.models import Vendor

# Create your models here.


class VPS(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    pack = models.CharField(max_length=60, null=True)
    vcpu = models.IntegerField(null=True)
    ssd = models.IntegerField(null=True)
    ram = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price_1 = models.IntegerField(null=True)
    price_3 = models.IntegerField(null=True)
    price_6 = models.IntegerField(null=True)
    price_12 = models.IntegerField(null=True)
    price_1_usd = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price_3_usd = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price_6_usd = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price_12_usd = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    link = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.vendor.name + ' ' + self.pack