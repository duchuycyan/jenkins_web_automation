import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://tenten.vn/"
urls = "https://tenten.vn/vi/bang-gia-ten-mien"
source = "TenTen"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll("td", text=".vn")
    reg_origin = mark_origin[0].parent.contents[11].text.strip("\n đ").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin[0].parent.contents[13].text.strip("\n đ").replace('.', '')
    trans_price = mark_origin[1].parent.contents[9].text.strip("\n đ").replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll("td", text=".com.vn | .net.vn | .biz.vn")
    reg_origin = mark_origin[0].parent.contents[11].text.strip("\n đ").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin[0].parent.contents[13].text.strip("\n đ").replace('.', '')
    trans_price = mark_origin[1].parent.contents[9].text.strip("\n đ").replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_com():
    dom_origin = get_dom(homepage)
    mark_origin = dom_origin.find('p', text='.com').parent
    reg_origin = int(mark_origin.contents[4].text.replace('k', '000')) * 110 // 100
    reg_promotion = int(mark_origin.contents[3].text.replace('k', '000')) * 110 // 100
    dom = get_dom(urls)
    mark = dom.find(class_="k_bgtm k_tmqt").table.tbody
    renew_price = int(mark.contents[1].contents[6].text.strip("\n đ").replace('.', '')) * 110 // 100
    trans_price = int(mark.contents[1].contents[8].text.strip("\n đ").replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(homepage)
    mark_origin = dom_origin.find('p', text='.net').parent
    reg_origin = int(mark_origin.contents[4].text.replace('k', '000')) * 110 // 100
    reg_promotion = int(mark_origin.contents[3].text.replace('k', '000')) * 110 // 100
    dom = get_dom(urls)
    mark = dom.find(class_="k_bgtm k_tmqt").table.tbody
    renew_price = int(mark.contents[5].contents[6].text.strip("\n đ").replace('.', '')) * 110 // 100
    trans_price = int(mark.contents[5].contents[8].text.strip("\n đ").replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(class_="k_bgtm k_tmqt").table.tbody
    reg_origin = int(mark_origin.contents[43].contents[4].text.strip("\n đ").replace('.', '')) * 110 // 100
    reg_promotion = reg_origin
    renew_price = int(mark_origin.contents[43].contents[6].text.strip("\n đ").replace('.', ''))  * 110 // 100
    trans_price = int(mark_origin.contents[43].contents[8].text.strip("\n đ").replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(homepage)
    mark_origin = dom_origin.find('p', text='.info').parent
    reg_origin = int(mark_origin.contents[4].text.replace('k', '000')) * 110 // 100
    reg_promotion = int(mark_origin.contents[3].text.replace('k', '000')) * 110 // 100
    dom = get_dom(urls)
    mark = dom.find(class_="k_bgtm k_tmqt").table.tbody
    renew_price = int(mark.contents[7].contents[6].text.strip("\n đ").replace('.', '')) *110 // 100
    try:
        trans_price = int(mark.contents[7].contents[8].text.strip("\n đ").replace('.', '')) * 110 // 100
    except:
        trans_price = int(mark.contents[7].contents[8].contents[0][:3] + '000') * 110 // 100
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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='TenTen'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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

        
    

        