import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.domain.com/"
urls = "https://www.domain.com/domains/extension-popup"
source = "Domain.com"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_rate():
    page = requests.get("https://www.freeforexapi.com/api/live?pairs=USDVND").text
    dic = json.loads(page)
    return dic['rates']["USDVND"]['rate']

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"rel": ".com"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin_usd = str(mark_origin_parent.find(class_="registration-price").string.strip().strip('$ per year'))
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = str(mark_origin_parent.find(class_="renewal-price").string.strip().strip('$ per year'))
    renew_price = round(float(renew_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, renew_price, reg_origin_usd, reg_promotion_usd, renew_price_usd]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"rel": ".net"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin_usd = str(mark_origin_parent.find(class_="registration-price").string.strip().strip('$ per year'))
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = str(mark_origin_parent.find(class_="renewal-price").string.strip().strip('$ per year'))
    renew_price = round(float(renew_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, renew_price, reg_origin_usd, reg_promotion_usd, renew_price_usd]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"rel": ".org"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin_usd = str(mark_origin_parent.find(class_="registration-price").string.strip().strip('$ per year'))
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = str(mark_origin_parent.find(class_="renewal-price").string.strip().strip('$ per year'))
    renew_price = round(float(renew_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, renew_price, reg_origin_usd, reg_promotion_usd, renew_price_usd]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"rel": ".info"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin_usd = str(mark_origin_parent.find(class_="registration-price").string.strip().strip('$ per year'))
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = str(mark_origin_parent.find(class_="renewal-price").string.strip().strip('$ per year'))
    renew_price = round(float(renew_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, renew_price, reg_origin_usd, reg_promotion_usd, renew_price_usd]


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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Domain.com'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'renew_price_usd': lst[5]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Domain.com'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'renew_price_usd': lst[5]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Domain.com'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'renew_price_usd': lst[5]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Domain.com'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'renew_price_usd': lst[5]})
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