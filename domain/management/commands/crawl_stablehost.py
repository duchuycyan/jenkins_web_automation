import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.stablehost.com/"
urls = "https://www.stablehost.com/domains-pricing.php"
source = "StableHost"

def get_dom(url):
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    page = requests.get(url, headers=headers)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_rate():
    page = requests.get("https://www.freeforexapi.com/api/live?pairs=USDVND").text
    dic = json.loads(page)
    return dic['rates']["USDVND"]['rate']

def get_com():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".COM").parent
    reg_origin_usd = mark_reg.contents[1].string.strip('').strip('$ ')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = mark_reg.contents[2].string.strip('').strip('$ ')
    renew_price = round(float(renew_price_usd) * get_rate())
    trans_price_usd = mark_reg.contents[3].string.strip('').strip('$ ')
    trans_price = round(float(trans_price_usd) * get_rate())
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]
 

def get_net():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".NET").parent
    reg_origin_usd = mark_reg.contents[1].string.strip('').strip('$ ')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = mark_reg.contents[2].string.strip('').strip('$ ')
    renew_price = round(float(renew_price_usd) * get_rate())
    trans_price_usd = mark_reg.contents[3].string.strip('').strip('$ ')
    trans_price = round(float(trans_price_usd) * get_rate())
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]

def get_org():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".ORG").parent
    reg_origin_usd = mark_reg.contents[1].string.strip('').strip('$ ')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = mark_reg.contents[2].string.strip('').strip('$ ')
    renew_price = round(float(renew_price_usd) * get_rate())
    trans_price_usd = mark_reg.contents[3].string.strip('').strip('$ ')
    trans_price = round(float(trans_price_usd) * get_rate())
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]

def get_info():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".INFO").parent
    reg_origin_usd = mark_reg.contents[1].string.strip('').strip('$ ')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = mark_reg.contents[2].string.strip('').strip('$ ')
    renew_price = round(float(renew_price_usd) * get_rate())
    trans_price_usd = mark_reg.contents[3].string.strip('').strip('$ ')
    trans_price = round(float(trans_price_usd) * get_rate())
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]



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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='StableHost'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='StableHost'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='StableHost'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='StableHost'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
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