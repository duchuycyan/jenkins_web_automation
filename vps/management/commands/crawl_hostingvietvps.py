import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://hostingviet.vn/"
urls_1 = "https://hostingviet.vn/vps-starter-gia-re"
urls_2 = "https://hostingviet.vn/vps-chuyen-nghiep"
urls_3 = "https://hostingviet.vn/vps-cao-cap"
source = "HostingViet"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom


def get_pack_1():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_3, price_6, price_12, urls_1]

def get_pack_2():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_3, price_6, price_12, urls_1]

def get_pack_3():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][10:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_1]

def get_pack_4():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[3]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][10:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_1]

def get_pack_5():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_6():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_7():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_8():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]

def get_pack_9():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]

def get_pack_10():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]


class Command(BaseCommand):
    help = 'Crawl PriceList'
  

    def handle(self, *args, **kwargs):
        def new_pack_1():
            lst = get_pack_1()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_3': lst[4], 'price_6': lst[5], 'price_12': lst[6], 'link': lst[7]})
        def new_pack_2():
            lst = get_pack_2()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_3': lst[4], 'price_6': lst[5], 'price_12': lst[6], 'link': lst[7]})
        def new_pack_3():
            lst = get_pack_3()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_5()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_6()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_7():
            lst = get_pack_7()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8():
            lst = get_pack_8()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_9():
            lst = get_pack_9()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_10():
            lst = get_pack_10()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostingViet'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        
        
        new_pack_1()
        new_pack_2()
        new_pack_3()
        new_pack_4()
        new_pack_5()
        new_pack_6()
        new_pack_7()
        new_pack_8()
        new_pack_9()
        new_pack_10()