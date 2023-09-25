import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://vinahost.vn/"
urls = "https://vinahost.vn/bang-gia-ten-mien.html"
source = "VinaHost"

def get_dom(url):
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    page = requests.get(url, headers=header)
    dom = BeautifulSoup(page.text, "html5lib")
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".vn").parent
    reg_origin = mark_origin.contents[11].string.strip(" VNĐ").replace(",", "")
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[13].string.strip(" VNĐ").replace(",", "")
    return [reg_origin, reg_promotion, renew_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".com.vn | .net.vn | .biz.vn").parent
    reg_origin = mark_origin.contents[11].string.strip(" VNĐ").replace(",", "")
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[13].string.strip(" VNĐ").replace(",", "")
    return [reg_origin, reg_promotion, renew_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".com | .com.co | .cc | .xyz").parent
    reg_origin = mark_origin.contents[3].string.strip(" VNĐ/năm").replace(",", "")
    reg_promotion = reg_origin
    trans_price = mark_origin.contents[5].string.strip(" VNĐ/năm").replace(",", "")
    return [reg_origin, reg_promotion, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".net").parent
    reg_origin = mark_origin.contents[3].string.strip(" VNĐ/năm").replace(",", "")
    reg_promotion = reg_origin
    trans_price = mark_origin.contents[5].string.strip(" VNĐ/năm").replace(",", "")
    return [reg_origin, reg_promotion, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".org").parent
    reg_origin = mark_origin.contents[3].string.strip(" VNĐ/năm").replace(",", "")
    reg_promotion = reg_origin
    trans_price = mark_origin.contents[5].string.strip(" VNĐ/năm").replace(",", "")
    return [reg_origin, reg_promotion, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".info").parent
    reg_origin = mark_origin.contents[3].string.strip(" VNĐ/năm").replace(",", "")
    reg_promotion = reg_origin
    trans_price = mark_origin.contents[5].string.strip(" VNĐ/năm").replace(",", "")
    return [reg_origin, reg_promotion, trans_price]


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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='VinaHost'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'trans_price': lst[2]})
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

        