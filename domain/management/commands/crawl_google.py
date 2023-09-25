import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor


homepage = "https://domains.google/"
urls = "https://domains-goog-prod.storage.googleapis.com/data/pricing/domains.us.json?cb=1582564985336"
source = "Google"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_rate():
    page = requests.get("https://www.freeforexapi.com/api/live?pairs=USDVND").text
    dic = json.loads(page)
    return dic['rates']["USDVND"]['rate']

def get_com():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin_usd = str(int(lst_json['data'][47]['price'])) + '.00'
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    return [reg_origin, reg_promotion, reg_origin_usd, reg_promotion_usd]

def get_net():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin_usd = str(int(lst_json['data'][179]['price'])) + '.00'
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    return [reg_origin, reg_promotion, reg_origin_usd, reg_promotion_usd]

def get_org():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin_usd = str(int(lst_json['data'][185]['price'])) + '.00'
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    return [reg_origin, reg_promotion, reg_origin_usd, reg_promotion_usd]

def get_info():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    reg_origin_usd = str(int(lst_json['data'][140]['price'])) + '.00'
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    return [reg_origin, reg_promotion, reg_origin_usd, reg_promotion_usd]


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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Google'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'reg_origin_usd': lst[2], 'reg_promotion_usd': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Google'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'reg_origin_usd': lst[2], 'reg_promotion_usd': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Google'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'reg_origin_usd': lst[2], 'reg_promotion_usd': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Google'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'reg_origin_usd': lst[2], 'reg_promotion_usd': lst[3]})
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