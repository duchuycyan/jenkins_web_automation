import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.pavietnam.vn/"
urls = "https://www.pavietnam.vn/en/ten-mien-bang-gia.html"
sale_url = "https://www.pavietnam.vn/en/uu-dai-ten-mien-viet-nam.html"
source = "P.A VietNam"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_sale = get_dom(sale_url)
    mark_sale = dom_sale.find("strong", text=".VN")
    reg_promotion = int(mark_sale.nextSibling.nextSibling.string + "000") + 10000
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll(attrs={"lang": "abcdefg_vn"})
    reg_origin = str(round(float(mark_origin[0].contents[0].strip()) + float(mark_origin[1].contents[0].strip()) + \
        float(mark_origin[1].parent.nextSibling.nextSibling.contents[0].strip()) * 110 // 100)) + '000'
    renew_price = str(round(float(mark_origin[1].contents[0].strip()) + \
        float(mark_origin[1].parent.nextSibling.nextSibling.nextSibling.nextSibling.contents[0].strip()) * 110 // 100)) + '000'
    trans_price = str(round(float(mark_origin[2].contents[0].strip()) + float(mark_origin[3].contents[0].strip()) * 110 // 100)) + '000'
    note = "Áp dụng thứ 3 và thứ 4"
    return [reg_origin, reg_promotion, renew_price, trans_price, note]

def get_comvn():
    dom_sale = get_dom(sale_url)
    mark_sale = dom_sale.find("strong", text=".COM.VN")
    reg_promotion = int(mark_sale.nextSibling.nextSibling.string + "000") + 10000
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll(attrs={"lang": "abcdefg_com_vn"})
    reg_origin = str(round(float(mark_origin[0].contents[0].strip()) + float(mark_origin[1].contents[0].strip()) + \
        float(mark_origin[1].parent.nextSibling.nextSibling.contents[0].strip()) * 110 // 100)) + '000'
    renew_price = str(round(float(mark_origin[1].contents[0].strip()) + \
        float(mark_origin[1].parent.nextSibling.nextSibling.nextSibling.nextSibling.contents[0].strip()) * 110 // 100)) + '000'
    trans_price = str(round(float(mark_origin[2].contents[0].strip()) + float(mark_origin[3].contents[0].strip()) * 110 // 100)) + '000'  
    note = "Áp dụng thứ 3 và thứ 4"
    return [reg_origin, reg_promotion, renew_price, trans_price, note]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "com"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin = mark_origin_parent.contents[5].contents[1].text.strip("d").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin_parent.contents[7].contents[1].text.strip(" d").replace('.', '')
    trans_price = mark_origin_parent.contents[9].contents[1].contents[0].strip().replace('.', '')
    note = "Giá ưu đãi chỉ áp dụng cho năm đầu tiên khi khách hàng đăng ký tên miền từ 2 năm trở lên"
    return [reg_origin, reg_promotion, renew_price, trans_price, note]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "net"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin = mark_origin_parent.contents[5].contents[1].text.strip("d").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin_parent.contents[7].contents[1].text.strip(" d").replace('.', '')
    trans_price = mark_origin_parent.contents[9].contents[1].contents[0].strip().replace('.', '')
    note = "Giá ưu đãi chỉ áp dụng cho năm đầu tiên khi khách hàng đăng ký tên miền từ 2 năm trở lên"
    return [reg_origin, reg_promotion, renew_price, trans_price, note]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "org"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin = mark_origin_parent.contents[5].contents[1].text.strip("d").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin_parent.contents[7].contents[1].text.strip(" d").replace('.', '')
    trans_price = mark_origin_parent.contents[9].contents[1].contents[0].strip().replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "info"})
    mark_origin_parent = mark_origin.parent.parent
    reg_origin = mark_origin_parent.contents[5].contents[1].text.strip("d").replace('.', '')
    reg_promotion = reg_origin
    renew_price = mark_origin_parent.contents[7].contents[1].text.strip(" d").replace('.', '')
    trans_price = mark_origin_parent.contents[9].contents[1].contents[0].strip().replace('.', '')
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
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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

        