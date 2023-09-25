from django.shortcuts import render
from vps.models import VPS
# Create your views here.

def index(request):
    val = request.GET.get('sort')
    if val == None:
        lst_pack = VPS.objects.all().order_by('vendor__name', 'price_3').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'vcpu-asc':
        lst_pack = VPS.objects.all().order_by('vcpu', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'vcpu-desc':
        lst_pack = VPS.objects.all().order_by('-vcpu', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'ssd-asc':
        lst_pack = VPS.objects.all().order_by('ssd', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'ssd-desc':
        lst_pack = VPS.objects.all().order_by('-ssd', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'ram-asc':
        lst_pack = VPS.objects.all().order_by('ram', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    elif val == 'ram-desc':
        lst_pack = VPS.objects.all().order_by('-ram', 'vendor__name').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link')
    return render(request, 'vps/vps.html', {'list_pack': lst_pack, 'val': val})

