import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.exabytes.com/"
source = "Exabytes"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_rate():
    page = requests.get("https://www.freeforexapi.com/api/live?pairs=USDVND").text
    dic = json.loads(page)
    return dic['rates']["USDVND"]['rate']

def get_com():
    dom_reg = get_dom("https://www.exabytes.com/domains/domain-name-search")
    mark_reg = dom_reg.find(class_="caption_column column_0_responsive")
    reg_origin_usd = mark_reg.contents[0].contents[3].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    dom_trans = get_dom("https://www.exabytes.com/domains/domain-transfer")
    mark_trans = dom_trans.find(class_="column_1 column_1_responsive")
    trans_price_usd = mark_trans.contents[0].contents[3].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    trans_price = round(float(trans_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, trans_price, reg_origin_usd, reg_promotion_usd, trans_price_usd]

def get_net():
    dom_reg = get_dom("https://www.exabytes.com/domains/domain-name-search")
    mark_reg = dom_reg.find(class_="column_1 column_1_responsive")
    reg_origin_usd = mark_reg.contents[0].contents[3].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    dom_trans = get_dom("https://www.exabytes.com/domains/domain-transfer")
    mark_trans = dom_trans.find(class_="column_1 column_1_responsive")
    trans_price_usd = mark_trans.contents[0].contents[4].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    trans_price = round(float(trans_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, trans_price, reg_origin_usd, reg_promotion_usd, trans_price_usd]

def get_org():
    dom_reg = get_dom("https://www.exabytes.com/domains/domain-name-search")
    mark_reg = dom_reg.find(class_="column_3 column_3_responsive")
    reg_origin_usd = mark_reg.contents[0].contents[3].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    dom_trans = get_dom("https://www.exabytes.com/domains/domain-transfer")
    mark_trans = dom_trans.find(class_="column_1 column_1_responsive")
    trans_price_usd = mark_trans.contents[0].contents[5].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    trans_price = round(float(trans_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, trans_price, reg_origin_usd, reg_promotion_usd, trans_price_usd]

def get_info():
    dom_reg = get_dom("https://www.exabytes.com/domains/domain-name-search")
    mark_reg = dom_reg.find(class_="column_2 column_2_responsive")
    reg_origin_usd = mark_reg.contents[0].contents[4].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    dom_trans = get_dom("https://www.exabytes.com/domains/domain-transfer")
    mark_trans = dom_trans.find(class_="column_1 column_1_responsive")
    trans_price_usd = mark_trans.contents[0].contents[4].contents[0].contents[0].contents[0].contents[1].string.strip('$/yr')
    trans_price = round(float(trans_price_usd)  * get_rate())
    return [reg_origin, reg_promotion, trans_price, reg_origin_usd, reg_promotion_usd, trans_price_usd]


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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Exabytes'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'trans_price_usd': lst[5]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Exabytes'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'trans_price_usd': lst[5]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Exabytes'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'trans_price_usd': lst[5]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Exabytes'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2], 'reg_origin_usd': lst[3], 'reg_promotion_usd': lst[4], 'trans_price_usd': lst[5]})
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