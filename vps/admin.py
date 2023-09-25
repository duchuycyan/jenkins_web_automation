from django.contrib import admin
from .models import VPS
# Register your models here.


class VPSAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'pack', 'price_1', 'vcpu', 'ssd', 'ram']
    list_filter = ['vendor']
    search_fields = ['vendor']
    fieldsets = [
        ('Nhà cung cấp', {'fields': ['vendor']}),
        ('Gói', {'fields': ['pack']}),
        ('vCPU (Cores)', {'fields': ['vcpu']}),
        ('SSD (GB)', {'fields': ['ssd']}),
        ('RAM (GB)', {'fields': ['ram']}),
        ('Giá 1 tháng (VND/USD)', {'fields': ['price_1', 'price_1_usd']}),
        ('Giá 3 tháng (VND/USD)', {'fields': ['price_3', 'price_3_usd']}),
        ('Giá 6 tháng (VND/USD)', {'fields': ['price_6', 'price_6_usd']}),
        ('Giá 12 tháng (VND/USD)', {'fields': ['price_12', 'price_12_usd']}),
        ('Link đăng ký', {'fields': ['link']}),
        ('Ghi chú', {'fields': ['note']}),
    ]

admin.site.register(VPS, VPSAdmin)