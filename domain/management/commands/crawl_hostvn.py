import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://hostvn.net/"
urls = "https://hostvn.net/wp-admin/admin-ajax.php?action=domain-extension"
source = "HostVN"

def get_vn():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[57]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[57]['renew'] * 110 // 100)
    return [reg_origin, reg_promotion, renew_price]

def get_comvn():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[58]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[58]['renew'] * 110 // 100)
    # trans_price = str(lst_json[58]['transfer'])
    return [reg_origin, reg_promotion, renew_price]

def get_com():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[0]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[0]['renew'] * 110 // 100)
    trans_price = str(lst_json[0]['transfer'] * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[1]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[1]['renew'] * 110 // 100)
    trans_price = str(lst_json[1]['transfer'] * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[2]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[2]['renew'] * 110 // 100)
    trans_price = str(lst_json[2]['transfer'] * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = str(lst_json[54]['price'] * 110 // 100)
    reg_promotion = reg_origin
    renew_price = str(lst_json[54]['renew'] * 110 // 100)
    trans_price = str(lst_json[54]['transfer'] * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-vn',action='store_true', help='crawl .vn')
        parser.add_argument('-comvn',action='store_true', help='crawl .com.vn')
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        def new_vn():
            lst = get_vn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        if kwargs['vn']:
            new_vn()
        elif kwargs['comvn']:
            new_comvn()
        elif kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_vn()
            new_comvn()
            new_com()
            new_net()
            new_org()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")

        