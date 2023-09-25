import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.crazydomains.com/"
urls = "https://www.crazydomains.com/domain-names/"
source = "Crazy Domain"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find(attrs={'id': 'tld_dom_com'})
    reg_origin = mark_reg.find(class_="sale_price").string.replace(",", "")
    reg_promotion = reg_origin
    renew_price = reg_origin
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price]
 
def get_net():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find(attrs={'id': 'tld_dom_net'})
    reg_origin = mark_reg.find(class_="sale_price").string.replace(",", "")
    reg_promotion = reg_origin
    renew_price = reg_origin
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find(attrs={'id': 'tld_dom_org'})
    reg_origin = mark_reg.find(class_="sale_price").string.replace(",", "")
    reg_promotion = reg_origin
    renew_price = reg_origin
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find(attrs={'id': 'tld_dom_info'})
    reg_origin = mark_reg.find(class_="sale_price").string.replace(",", "")
    reg_promotion = reg_origin
    renew_price = reg_origin
    trans_price = reg_origin
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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Crazy Domain'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Crazy Domain'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Crazy Domain'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Crazy Domain'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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