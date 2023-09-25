import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://hostvn.net/"
urls = "https://hostvn.net/cloud/cloud-vps/"
source = "HostVN"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_512():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[0]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip(' MB')) / 1024)
    price_1 = mark.find(attrs={'id': 'selectPackagePrice1'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice1'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice1'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice1'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_1():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[1]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice2'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice2'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice2'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice2'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_2():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[2]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice3'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice3'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice3'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice3'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[3]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice4'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice4'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice4'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice4'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_6():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[4]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice5'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice5'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice5'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice5'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[5]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice6'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice6'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice6'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice6'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_12():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[6]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice7'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice7'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice7'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice7'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_16():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[7]
    pack = mark.h3.string
    vcpu = mark.find(class_="package-body").ul.contents[0].contents[2].text.strip()
    ssd = mark.find(class_="package-body").ul.contents[2].contents[2].text.strip(' GB')
    ram = mark.find(class_="package-body").ul.contents[1].contents[2].text.strip('GB')
    price_1 = mark.find(attrs={'id': 'selectPackagePrice8'}).contents[0].string[11:].strip('đ').replace('.', '')
    price_3 = mark.find(attrs={'id': 'selectPackagePrice8'}).contents[1].string[11:].strip('đ').replace('.', '')
    price_6 = mark.find(attrs={'id': 'selectPackagePrice8'}).contents[2].string[11:].strip('đ').replace('.', '')
    price_12 = mark.find(attrs={'id': 'selectPackagePrice8'}).contents[3].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]


class Command(BaseCommand):
    help = 'Crawl PriceList'


    def handle(self, *args, **kwargs):
        def new_pack_512():
            lst = get_pack_512()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_1():
            lst = get_pack_1()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_2():
            lst = get_pack_2()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_6()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8():
            lst = get_pack_8()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_12():
            lst = get_pack_12()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_16():
            lst = get_pack_16()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='HostVN'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        
        new_pack_512()
        new_pack_1()
        new_pack_2()
        new_pack_4()
        new_pack_6()
        new_pack_8()
        new_pack_12()
        new_pack_16()