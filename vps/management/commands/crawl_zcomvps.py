import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://cloud.z.com/"
urls = "https://cloud.z.com/vn/en/"
source = "Z.com"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_1():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[1]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_2():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[3]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_3():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[5]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[7]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_5():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[9]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_6():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[11]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_7():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[13]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[15]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_9():
    dom = get_dom(urls)
    mark = dom.find(class_="MS-content").contents[17]
    pack = mark.find('h2').string
    vcpu = mark.find('ul').contents[1].string.strip('CPU Core')
    ssd = mark.find('ul').contents[5].string.strip('SSD GB')
    ram = mark.find('ul').contents[3].string.strip('RAM GB')
    price_1 = int(mark.find('h4').b.string.replace('.', ''))
    price_3 = price_1 * 3
    price_6 = price_1 * 6
    price_12 = price_1 * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]


class Command(BaseCommand):
    help = 'Crawl PriceList'
  

    def handle(self, *args, **kwargs):
        def new_pack_1():
            lst = get_pack_1()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_2():
            lst = get_pack_2()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_3():
            lst = get_pack_3()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_5()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_6()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_7():
            lst = get_pack_7()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8():
            lst = get_pack_8()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_9():
            lst = get_pack_9()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='Z.com'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        

        new_pack_1()
        new_pack_2()
        new_pack_3()
        new_pack_4()
        new_pack_5()
        new_pack_6()
        new_pack_7()
        new_pack_8()
        new_pack_9()