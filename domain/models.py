from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20, unique=True)
    homepage = models.CharField(max_length=30, unique=True)
    vendor_location_choices = [
        ('FOR', 'Foreign'),
        ('VN', 'VietNam')
    ]
    vendor_location = models.CharField(
        max_length=10,
        choices=vendor_location_choices,
        default='VN',
    )
    logo = models.CharField(max_length=30, unique=True, null=True)
    def __str__(self):
        return self.name

class Domain(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    domain_type_choices = [
        ('vn', '.vn'),
        ('com', '.com'),
        ('comvn', '.com.vn'),
        ('net', '.net'),
        ('org', '.org'),
        ('info', '.info'),
    ]
    domain_type = models.CharField(
        max_length=10,
        choices=domain_type_choices,
        default='vn',
    )
    reg_origin = models.IntegerField(null=True)
    reg_origin_usd = models.CharField(max_length=10, blank=True)
    reg_promotion = models.IntegerField(null=True)
    reg_promotion_usd = models.CharField(max_length=10, blank=True)
    renew_price = models.IntegerField(null=True)
    renew_price_usd = models.CharField(max_length=10, blank=True)
    trans_price = models.IntegerField(null=True)
    trans_price_usd = models.CharField(max_length=10, blank=True)
    rates = models.CharField(max_length=10, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.vendor.name + ' ' + self.domain_type

# class Hosting(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     price = models.CharField(max_length=20, default="0")
#     quotes = models.CharField(max_length=20, default="0")
#     bandwidths = models.CharField(max_length=20, default="0")
#     def __str__(self):
#         return self.vendor.name + 'Hosting'
