import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.tnd.vn/"
urls = "https://cloud.tnd.vn/widgets/domainpricelist.php"
source = "TND"

def get_dom(url):
    page = requests.get(urls).text.strip(r"document.write('\n").strip("');")
    dom = BeautifulSoup(page, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.vn').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.com.vn').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.com').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.net').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.org').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text='.info').parent
    reg_origin = mark_origin.contents[1].contents[1].string.replace(',', '').strip('đ')
    reg_promotion = reg_origin
    renew_price = mark_origin.contents[2].contents[1].string.replace(',', '').strip('đ')
    trans_price = mark_origin.contents[3].contents[1].string.replace(',', '').strip('đ')
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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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
