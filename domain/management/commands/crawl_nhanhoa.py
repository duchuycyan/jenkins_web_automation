import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://nhanhoa.com/"
urls = "https://nhanhoa.com/trang/ten-mien/bang-gia-ten-mien.html"
source = "NhanHoa"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll('td', text=".vn")[0].parent
    reg_origin = mark_origin.contents[11].text.strip(" đ").replace('.', '')
    renew_price = mark_origin.contents[13].text.strip(" đ").replace('.', '')
    mark_trans = dom_origin.findAll('td', text=".vn")[1].parent
    trans_price = mark_trans.contents[9].string.strip(' đ').replace('.', '')
    dom_sale = get_dom(homepage)
    try:
        mark_sale = dom_sale.find(attrs={"src": "templates/images/domain/d1.jpg"}).parent.parent
        reg_promotion = int(mark_sale.find(class_="option-new").text.replace('K', '000')) + 10000
        note = mark_sale.find(class_="title-saveoff-1").text
        return [reg_origin, reg_promotion, renew_price, trans_price, note]
    except:
        mark_sale = dom_sale.find("figure", text=".vn")
        mark_sale_sibling = mark_sale.nextSibling.nextSibling
        reg_promotion = mark_sale_sibling.p.text.strip(" đ").replace('.', '')
        return [reg_origin, reg_promotion, renew_price, trans_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".com").parent
    reg_origin = int(mark_origin.contents[2].contents[0].text.strip(' đ').replace('.', '')) * 110 // 100
    renew_price = reg_origin
    trans_price = int(mark_origin.contents[3].string.strip(' đ').replace('.', '')) * 110 // 100
    dom_sale = get_dom(homepage)
    try:
        mark_sale = dom_sale.find(attrs={"src": "templates/images/domain/d2.jpg"}).parent.parent
        reg_promotion = int(mark_sale.find(class_="option-new").text.replace('K', '000')) * 110 // 100
        note = mark_sale.find(class_="title-saveoff-1").text
        return [reg_origin, reg_promotion, renew_price, trans_price, note] 
    except:
        mark_sale = dom_sale.find("figure", text=".com")
        mark_sale_sibling = mark_sale.nextSibling.nextSibling
        reg_promotion = int(mark_sale_sibling.p.text.strip(' đ').replace('.', '')) * 110 // 100
        return [reg_origin, reg_promotion, renew_price, trans_price]   

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll('td', text=".net.vn/ .com.vn/ .biz.vn ")[0].parent
    reg_origin = mark_origin.contents[11].text.strip(" đ").replace('.', '')
    renew_price = mark_origin.contents[13].text.strip(" đ").replace('.', '')
    mark_trans = dom_origin.findAll('td', text=".net.vn/ .com.vn/ .biz.vn ")[1].parent
    trans_price = mark_trans.contents[9].string.strip(' đ').replace('.', '')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".com.vn")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    reg_promotion = int(mark_sale_sibling.p.text.strip(" đ").replace('.', '')) + 10000
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".net").parent
    reg_origin = int(mark_origin.contents[2].contents[0].text.strip(' đ').replace('.', '')) * 110 // 100
    renew_price = reg_origin
    trans_price = int(mark_origin.contents[3].string.strip(' đ').replace('.', '')) * 110 // 100
    dom_sale = get_dom(homepage)
    try:
        mark_sale = dom_sale.find(attrs={"src": "https://nhanhoa.com/uploads/attach/1578019237_net.png"}).parent.parent.parent
        reg_promotion = int(mark_sale.find(class_="option-new").text.replace('K', '000')) * 110 // 100
        note = mark_sale.find(class_="title-saveoff-2").text
        return [reg_origin, reg_promotion, renew_price, trans_price, note] 
    except:
        mark_sale = dom_sale.find("figure", text=".net")
        mark_sale_sibling = mark_sale.nextSibling.nextSibling
        reg_promotion = int(mark_sale_sibling.p.text.strip(' đ').replace('.', ''))
        return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".org").parent
    reg_origin = int(mark_origin.contents[2].contents[0].text.strip(' đ').replace('.', '')) * 110 // 100
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".org")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    reg_promotion = int(mark_sale_sibling.p.text.strip(' đ').replace('.', '')) * 110 // 100
    renew_price = reg_origin
    trans_price = int(mark_origin.contents[3].string.strip(' đ').replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".info").parent
    reg_origin = int(mark_origin.contents[2].contents[0].text.strip(' đ').replace('.', '')) * 110 // 100
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".info")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    reg_promotion = int(mark_sale_sibling.p.text.strip(' đ').replace('.', '')) * 110 // 100
    renew_price = reg_origin
    trans_price = int(mark_origin.contents[3].string.strip(' đ').replace('.', '')) * 110 // 100
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
            try:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'note': lst[4]})
            except:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            try:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'note': lst[4]})
            except:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            try:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'note': lst[4]})
            except:
                Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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
