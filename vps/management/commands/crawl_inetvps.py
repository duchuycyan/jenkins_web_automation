import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://inet.vn/"
urls = "https://inet.vn/vps"
urls_1 = "https://inet.vn/api/package/list/vps/cloud-new"
urls_2 = "https://inet.vn/api/category/vpsperiods"
source = "iNET"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

# def get_price_policy():
#     dom = requests.get(urls_2).text
#     lst_json = json.loads(dom)
#     percent_1 = 100 - int(lst_json[0]['discountPercent'])
#     percent_3 = 100 - int(lst_json[1]['discountPercent'])
#     percent_6 = 100 - int(lst_json[2]['discountPercent'])
#     percent_12 = 100 - int(lst_json[3]['discountPercent'])
#     return [percent_1, percent_3, percent_6, percent_12]


def get_pack_1():
    dom = requests.get(urls_1).text
    lst_json = json.loads(dom)['content']
    pack = lst_json[0]['name']
    hardware = BeautifulSoup(lst_json[0]['description'], 'html5lib').ul
    vcpu = hardware.contents[0].text.strip('CPU: Core')
    ssd = int(hardware.contents[2].contents[0].strip('SSD: GB +')) + int(hardware.contents[2].contents[1].text.strip('GB Free'))
    ram = hardware.contents[1].text.replace('RAM - DDR4: ', '').replace('GB', '')
    # lst_policy = get_price_policy()
    price_1 = (int(lst_json[0]['promotionPrice']) * 110 // 100) * 1
    price_3 = (int(lst_json[0]['promotionPrice']) * 110 // 100) * 3
    price_6 = (int(lst_json[0]['promotionPrice']) * 110 // 100) * 6
    price_12 = (int(lst_json[0]['promotionPrice']) * 110 // 100) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_2():
    dom = requests.get(urls_1).text
    lst_json = json.loads(dom)['content']
    pack = lst_json[1]['name']
    hardware = BeautifulSoup(lst_json[1]['description'], 'html5lib').ul
    vcpu = hardware.contents[0].text.strip('CPU: Core')
    ssd = int(hardware.contents[2].contents[0].strip('SSD: GB +')) + int(hardware.contents[2].contents[1].text.strip('GB Free'))
    ram = hardware.contents[1].text.replace('RAM - DDR4: ', '').replace('GB', '')
    # lst_policy = get_price_policy()
    price_1 = (int(lst_json[1]['promotionPrice']) * 110 // 100) * 1
    price_3 = (int(lst_json[1]['promotionPrice']) * 110 // 100) * 3
    price_6 = (int(lst_json[1]['promotionPrice']) * 110 // 100) * 6
    price_12 = (int(lst_json[1]['promotionPrice']) * 110 // 100) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_3():
    dom = requests.get(urls_1).text
    lst_json = json.loads(dom)['content']
    pack = lst_json[2]['name']
    hardware = BeautifulSoup(lst_json[2]['description'], 'html5lib').ul
    vcpu = hardware.contents[0].text.strip('CPU: Core')
    ssd = int(hardware.contents[2].contents[0].strip('SSD: GB +')) + int(hardware.contents[2].contents[1].text.strip('GB Free'))
    ram = hardware.contents[1].text.replace('RAM - DDR4: ', '').replace('GB', '')
    # lst_policy = get_price_policy()
    price_1 = (int(lst_json[2]['promotionPrice']) * 110 // 100) * 1
    price_3 = (int(lst_json[2]['promotionPrice']) * 110 // 100) * 3
    price_6 = (int(lst_json[2]['promotionPrice']) * 110 // 100) * 6
    price_12 = (int(lst_json[2]['promotionPrice']) * 110 // 100) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    dom = requests.get(urls_1).text
    lst_json = json.loads(dom)['content']
    pack = lst_json[3]['name']
    hardware = BeautifulSoup(lst_json[3]['description'], 'html5lib').ul
    vcpu = hardware.contents[0].text.strip('CPU: Core')
    ssd = int(hardware.contents[2].contents[0].strip('SSD: GB +')) + int(hardware.contents[2].contents[1].text.strip('GB Free'))
    ram = hardware.contents[1].text.replace('RAM - DDR4: ', '').replace('GB', '')
    # lst_policy = get_price_policy()
    price_1 = (int(lst_json[3]['promotionPrice']) * 110 // 100) * 1
    price_3 = (int(lst_json[3]['promotionPrice']) * 110 // 100) * 3
    price_6 = (int(lst_json[3]['promotionPrice']) * 110 // 100) * 6
    price_12 = (int(lst_json[3]['promotionPrice']) * 110 // 100) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_5():
    dom = requests.get(urls_1).text
    lst_json = json.loads(dom)['content']
    pack = lst_json[4]['name']
    hardware = BeautifulSoup(lst_json[4]['description'], 'html5lib').ul
    vcpu = hardware.contents[0].text.strip('CPU: Core')
    ssd = int(hardware.contents[2].contents[0].strip('SSD: GB +')) + int(hardware.contents[2].contents[1].text.strip('GB Free'))
    ram = hardware.contents[1].text.replace('RAM - DDR4: ', '').replace('GB', '')
    # lst_policy = get_price_policy()
    price_1 = (int(lst_json[4]['promotionPrice']) * 110 // 100) * 1
    price_3 = (int(lst_json[4]['promotionPrice']) * 110 // 100) * 3
    price_6 = (int(lst_json[4]['promotionPrice']) * 110 // 100) * 6
    price_12 = (int(lst_json[4]['promotionPrice']) * 110 // 100) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]


class Command(BaseCommand):
    help = 'Crawl PriceList'


    def handle(self, *args, **kwargs):
        def new_pack_1():
            lst = get_pack_1()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='INET'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_2():
            lst = get_pack_2()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='INET'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_3():
            lst = get_pack_3()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='INET'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='INET'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_5()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='INET'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        
        
        new_pack_1()
        new_pack_2()
        new_pack_3()
        new_pack_4()
        new_pack_5()
