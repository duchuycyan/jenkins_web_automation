import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://vn.godaddy.com/"
urls = "https://vn.godaddy.com/domains/domain-name-search"
source = "GoDaddy"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom("https://vn.godaddy.com/tlds/com-domain")
    reg_origin = dom_origin.find('strike').string.strip(' ₫').replace('.', '')
    reg_promotion = dom_origin.find(class_="text-purchase").string.strip(' ₫').replace('.', '')
    note = "Yêu cầu mua 2 năm. Thanh toán cho năm thứ hai với giá 378.000"
    return [reg_origin, reg_promotion, note]

def get_net():
    dom_origin = get_dom("https://vn.godaddy.com/tlds/net-domain")
    reg_origin = dom_origin.find('strike').string.strip(' ₫').replace('.', '')
    reg_promotion = dom_origin.find(class_="text-purchase").string.strip(' ₫').replace('.', '')
    return [reg_origin, reg_promotion]

def get_org():
    dom_origin = get_dom("https://vn.godaddy.com/tlds/org-domain")
    reg_origin = dom_origin.find('strike').string.strip(' ₫').replace('.', '')
    reg_promotion = dom_origin.find(class_="text-purchase").string.strip(' ₫').replace('.', '')
    return [reg_origin, reg_promotion]

def get_info():
    dom_origin = get_dom("https://vn.godaddy.com/tlds/info-domain")
    reg_origin = dom_origin.find('strike').string.strip(' ₫').replace('.', '')
    reg_promotion = dom_origin.find(class_="text-purchase").string.strip(' ₫').replace('.', '')
    return [reg_origin, reg_promotion]


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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'note': lst[2]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
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
