import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://azdigi.com/"
urls = "https://azdigi.com/dang-ky-ten-mien/"
source = "AZDIGI"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.com').parent.parent
    reg_origin = mark_origin.contents[1].string.strip(' đ').replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[3].string.strip(' đ').replace('.', '')
    trans_price = mark_origin.contents[2].string.strip(' đ').replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.net').parent.parent
    reg_origin = mark_origin.contents[1].string.strip(' đ').replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[3].string.strip(' đ').replace('.', '')
    trans_price = mark_origin.contents[2].string.strip(' đ').replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.info').parent.parent
    reg_origin = mark_origin.contents[1].string.strip(' đ').replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[3].string.strip(' đ').replace('.', '')
    trans_price = mark_origin.contents[2].string.strip(' đ').replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]


class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')
    

    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        if kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_com()
            new_net()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")
