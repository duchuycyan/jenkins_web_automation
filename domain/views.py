from django.shortcuts import render
from django.http import HttpResponse
from domain.models import Domain, Vendor

# Create your views here.

def index(request):
    lst_vn = Domain.objects.all().filter(domain_type='vn').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')
    lst_comvn = Domain.objects.all().filter(domain_type='comvn').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')
    lst_com = Domain.objects.all().filter(domain_type='com').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')
    lst_net = Domain.objects.all().filter(domain_type='net').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')
    lst_org = Domain.objects.all().filter(domain_type='org').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')
    lst_info = Domain.objects.all().filter(domain_type='info').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'reg_promotion_usd', 'note')

    count_vendor_vn = Domain.objects.all().filter(domain_type='vn', reg_promotion__isnull=False).count() - 3
    count_vendor_comvn = Domain.objects.all().filter(domain_type='comvn', reg_promotion__isnull=False).count() - 3
    count_vendor_com = Domain.objects.all().filter(domain_type='com', reg_promotion__isnull=False).count() - 3
    count_vendor_net = Domain.objects.all().filter(domain_type='net', reg_promotion__isnull=False).count() - 3
    count_vendor_org = Domain.objects.all().filter(domain_type='org', reg_promotion__isnull=False).count() - 3
    count_vendor_info = Domain.objects.all().filter(domain_type='info', reg_promotion__isnull=False).count() - 3

    lst_cheapest = [lst_com[0], lst_net[0], lst_org[0], lst_info[0], lst_comvn[0], lst_vn[0]]
    lst_second = [lst_com[1], lst_net[1], lst_org[1], lst_info[1], lst_comvn[1], lst_vn[1]]
    lst_third = [lst_com[2], lst_net[2], lst_org[2], lst_info[2], lst_comvn[2], lst_vn[2]]

    # lst_com_other = []
    # lst_net_other = []
    # lst_org_other = []
    # lst_info_other = []
    # lst_comvn_other = []
    # lst_vn_other = []

    # for x in range(0, count_vendor_com):
    #     y = x + 3
    #     lst_com_other.append(lst_com[y])

    # for x in range(0, count_vendor_net):
    #     y = x + 3
    #     lst_net_other.append(lst_net[y])

    # for x in range(0, count_vendor_org):
    #     y = x + 3
    #     lst_org_other.append(lst_org[y])

    # for x in range(0, count_vendor_info):
    #     y = x + 3
    #     lst_info_other.append(lst_info[y])

    # for x in range(0, count_vendor_comvn):
    #     y = x + 3
    #     lst_comvn_other.append(lst_comvn[y])

    # for x in range(0, count_vendor_vn):
    #     y = x + 3
    #     lst_vn_other.append(lst_vn[y])

    lst_count = [count_vendor_com, count_vendor_net, count_vendor_org, count_vendor_info, count_vendor_comvn, count_vendor_vn]
    lst_other = [lst_com, lst_net, lst_org, lst_info, lst_comvn, lst_vn]
    # lst_other = [lst_com_other, lst_net_other, lst_org_other, lst_info_other, lst_comvn_other, lst_vn_other]

#------------------------------------------------------------------------------------------------------------------------------------#

    ren_vn = Domain.objects.all().filter(domain_type='vn', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')
    ren_comvn = Domain.objects.all().filter(domain_type='comvn', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')
    ren_com = Domain.objects.all().filter(domain_type='com', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')
    ren_net = Domain.objects.all().filter(domain_type='net', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')
    ren_org = Domain.objects.all().filter(domain_type='org', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')
    ren_info = Domain.objects.all().filter(domain_type='info', renew_price__isnull=False).order_by('renew_price').values_list('renew_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'renew_price_usd')


    count_vendor_vn_renew = Domain.objects.all().filter(domain_type='vn', renew_price__isnull=False).count() - 3
    count_vendor_comvn_renew = Domain.objects.all().filter(domain_type='comvn', renew_price__isnull=False).count() - 3
    count_vendor_com_renew = Domain.objects.all().filter(domain_type='com', renew_price__isnull=False).count() - 3
    count_vendor_net_renew = Domain.objects.all().filter(domain_type='net', renew_price__isnull=False).count() - 3
    count_vendor_org_renew = Domain.objects.all().filter(domain_type='org', renew_price__isnull=False).count() - 3
    count_vendor_info_renew = Domain.objects.all().filter(domain_type='info', renew_price__isnull=False).count() - 3

    ren_cheapest = [ren_com[0], ren_net[0], ren_org[0], ren_info[0], ren_comvn[0], ren_vn[0]]
    ren_second = [ren_com[1], ren_net[1], ren_org[1], ren_info[1], ren_comvn[1], ren_vn[1]]
    ren_third = [ren_com[2], ren_net[2], ren_org[2], ren_info[2], ren_comvn[2], ren_vn[2]]

    # ren_com_other = []
    # ren_net_other = []
    # ren_org_other = []
    # ren_info_other = []
    # ren_comvn_other = []
    # ren_vn_other = []

    # for x in range(0, count_vendor_com_renew):
    #     y = x + 3
    #     ren_com_other.append(ren_com[y])

    # for x in range(0, count_vendor_net_renew):
    #     y = x + 3
    #     ren_net_other.append(ren_net[y])

    # for x in range(0, count_vendor_org_renew):
    #     y = x + 3
    #     ren_org_other.append(ren_org[y])

    # for x in range(0, count_vendor_info_renew):
    #     y = x + 3
    #     ren_info_other.append(ren_info[y])

    # for x in range(0, count_vendor_comvn_renew):
    #     y = x + 3
    #     ren_comvn_other.append(ren_comvn[y])

    # for x in range(0, count_vendor_vn_renew):
    #     y = x + 3
    #     ren_vn_other.append(ren_vn[y])

    ren_count = [count_vendor_com_renew, count_vendor_net_renew, count_vendor_org_renew, count_vendor_info_renew, count_vendor_comvn_renew, count_vendor_vn_renew]
    ren_other = [ren_com, ren_net, ren_org, ren_info, ren_comvn, ren_vn]
    # ren_other = [ren_com_other, ren_net_other, ren_org_other, ren_info_other, ren_comvn_other, ren_vn_other]

#------------------------------------------------------------------------------------------------------------------------------------#

    trans_vn = Domain.objects.all().filter(domain_type='vn', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')
    trans_comvn = Domain.objects.all().filter(domain_type='comvn', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')
    trans_com = Domain.objects.all().filter(domain_type='com', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')
    trans_net = Domain.objects.all().filter(domain_type='net', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')
    trans_org = Domain.objects.all().filter(domain_type='org', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')
    trans_info = Domain.objects.all().filter(domain_type='info', trans_price__isnull=False).order_by('trans_price').values_list('trans_price', 'vendor__name', 'vendor__logo', 'vendor__homepage', 'trans_price_usd')


    count_vendor_vn_trans = Domain.objects.all().filter(domain_type='vn', trans_price__isnull=False).count() - 3
    count_vendor_comvn_trans = Domain.objects.all().filter(domain_type='comvn', trans_price__isnull=False).count() - 3
    count_vendor_com_trans = Domain.objects.all().filter(domain_type='com', trans_price__isnull=False).count() - 3
    count_vendor_net_trans = Domain.objects.all().filter(domain_type='net', trans_price__isnull=False).count() - 3
    count_vendor_org_trans = Domain.objects.all().filter(domain_type='org', trans_price__isnull=False).count() - 3
    count_vendor_info_trans = Domain.objects.all().filter(domain_type='info', trans_price__isnull=False).count() - 3

    trans_cheapest = [trans_com[0], trans_net[0], trans_org[0], trans_info[0], trans_comvn[0], trans_vn[0]]
    trans_second = [trans_com[1], trans_net[1], trans_org[1], trans_info[1], trans_comvn[1], trans_vn[1]]
    trans_third = [trans_com[2], trans_net[2], trans_org[2], trans_info[2], trans_comvn[2], trans_vn[2]]

    # trans_com_other = []
    # trans_net_other = []
    # trans_org_other = []
    # trans_info_other = []
    # trans_comvn_other = []
    # trans_vn_other = []

    # for x in range(0, count_vendor_com_trans):
    #     y = x + 3
    #     trans_com_other.append(trans_com[y])

    # for x in range(0, count_vendor_net_trans):
    #     y = x + 3
    #     trans_net_other.append(trans_net[y])

    # for x in range(0, count_vendor_org_trans):
    #     y = x + 3
    #     trans_org_other.append(trans_org[y])

    # for x in range(0, count_vendor_info_trans):
    #     y = x + 3
    #     trans_info_other.append(trans_info[y])

    # for x in range(0, count_vendor_comvn_trans):
    #     y = x + 3
    #     trans_comvn_other.append(trans_comvn[y])

    # for x in range(0, count_vendor_vn_trans):
    #     y = x + 3
    #     trans_vn_other.append(trans_vn[y])

    trans_count = [count_vendor_com_trans, count_vendor_net_trans, count_vendor_org_trans, count_vendor_info_trans, count_vendor_comvn_trans, count_vendor_vn_trans]
    trans_other = [trans_com, trans_net, trans_org, trans_info, trans_comvn, trans_vn]
    
    # trans_other = [trans_com_other, trans_net_other, trans_org_other, trans_info_other, trans_comvn_other, trans_vn_other]

#------------------------------------------------------------------------------------------------------------------------------------#

    return render(request, 'domain/domain.html', {'lst_cheapest': lst_cheapest, 'lst_second': lst_second, 'lst_third': lst_third, 'lst_other': lst_other, 'lst_count': lst_count,
     'ren_cheapest': ren_cheapest, 'ren_second': ren_second, 'ren_third': ren_third, 'ren_other': ren_other, 'ren_count': ren_count,
      'trans_cheapest': trans_cheapest, 'trans_second': trans_second, 'trans_third': trans_third, 'trans_other': trans_other, 'trans_count': trans_count})


def search(request):
    return render(request, 'domain/domain.html')