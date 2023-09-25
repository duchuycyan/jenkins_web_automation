import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://domain.z.com/vn/en/"
urls = "https://domain.z.com/vn/cart/api/GetTldList/"
urls_trans = "https://domain.z.com/vn/cart/api/GetDomainTransferPriceList/"
source = "Z.com"

def get_com():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = lst_json[1]['year1'].replace('.', '')
    reg_promotion = reg_origin
    renew_price = lst_json[1]['preprice_year1'].replace('.', '')
    reg_promotion = reg_origin
    dom_trans = requests.get(urls_trans).text
    lst_json_trans = json.loads(dom_trans)
    trans_price = lst_json_trans[1]['price']
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = lst_json[3]['year1'].replace('.', '')
    reg_promotion = reg_origin
    renew_price = lst_json[3]['preprice_year1'].replace('.', '')
    reg_promotion = reg_origin
    dom_trans = requests.get(urls_trans).text
    lst_json_trans = json.loads(dom_trans)
    trans_price = lst_json_trans[3]['price']
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = lst_json[7]['year1'].replace('.', '')
    reg_promotion = reg_origin
    renew_price = lst_json[7]['preprice_year1'].replace('.', '')
    reg_promotion = reg_origin
    dom_trans = requests.get(urls_trans).text
    lst_json_trans = json.loads(dom_trans)
    trans_price = lst_json_trans[7]['price']
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin = lst_json[6]['year1'].replace('.', '')
    reg_promotion = reg_origin
    renew_price = lst_json[6]['preprice_year1'].replace('.', '')
    reg_promotion = reg_origin
    dom_trans = requests.get(urls_trans).text
    lst_json_trans = json.loads(dom_trans)
    trans_price = lst_json_trans[6]['price']
    return [reg_origin, reg_promotion, renew_price, trans_price]


class Command(BaseCommand):
    help = 'Crawl PriceList'


    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')


    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        if kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_com()
            new_net()
            new_org()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")
