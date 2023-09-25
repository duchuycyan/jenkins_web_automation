import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://www.tnd.vn/"
urls = "https://www.tnd.vn/cloud-vps/"
source = "TND"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_125():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[0]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_250():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[1]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_500():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[2]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_1000():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[3]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_2000():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[4]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4000():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[5]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8000():
    dom = get_dom(urls)
    mark = dom.findAll(class_="planbox")[6]
    pack = mark.find('h2').string.strip()
    vcpu = mark.find('ul').contents[0].string.strip(' CPU')
    ssd = mark.find('ul').contents[2].string.strip(' GB SSD Enterprise')
    ram = mark.find('ul').contents[1].string.replace(' GB Ram DDR4', '')
    price_1 = mark.find('strong').contents[0].strip().replace('đ', '').replace(',', '')
    price_3 = int(price_1) * 3
    price_6 = int(price_1) * 6
    price_12 = int(price_1) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]


class Command(BaseCommand):
    help = 'Crawl PriceList'
  

    def handle(self, *args, **kwargs):
        def new_pack_125():
            lst = get_pack_125()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_250():
            lst = get_pack_250()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_500():
            lst = get_pack_500()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_1000():
            lst = get_pack_1000()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_2000():
            lst = get_pack_2000()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4000():
            lst = get_pack_4000()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8000():
            lst = get_pack_8000()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='TND'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        
        
        new_pack_125()
        new_pack_250()
        new_pack_500()
        new_pack_1000()
        new_pack_2000()
        new_pack_4000()
        new_pack_8000()
