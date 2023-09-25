import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from vps.models import VPS

homepage = "https://www.bkns.vn/"
urls = "https://www.bkns.vn/server/may-chu-ao.html"
source = "BKNS"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_price_policy():
    dom = get_dom(urls)
    mark = dom.find(class_='percent-discount clearfix')
    discount_6 = 100 - int(mark.ul.contents[0].find('span').string.strip('-%'))
    discount_12 = 100 - int(mark.ul.contents[1].find('span').string.strip('-%'))
    return [discount_6, discount_12]

def get_pack_1():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[0]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    return [pack, vcpu, ssd, ram, price_3, price_6, price_12, urls]
   
def get_pack_2():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[1]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_3():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[2]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[3]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_5():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[4]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_6():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[5]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_7():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[6]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8():
    lst_discount = get_price_policy()
    dom = get_dom(urls)
    mark = dom.find(class_="default-tp-ul default-tp-ul-show").contents[7]
    pack = mark.find('h3').string
    vcpu = mark.contents[0].contents[3].contents[0].contents[3].strip(' Core')
    ssd = mark.contents[0].contents[3].contents[2].contents[3].strip(' GB')
    ram = mark.contents[0].contents[3].contents[1].contents[3].strip(' GB')
    price_12 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) * 12
    price_3 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * 100 * 3
    price_6 = int(mark.find(class_="default-tp--price clearfix").string.strip('₫ /tháng').replace('.', '')) // lst_discount[1] * lst_discount[0] * 6
    price_1 = price_3 // 3
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]


class Command(BaseCommand):
    help = 'Crawl PriceList'
  

    def handle(self, *args, **kwargs):
        def new_pack_1():
            lst = get_pack_1()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_3': lst[4], 'price_6': lst[5], 'price_12': lst[6], 'link': lst[7]})
        def new_pack_2():
            lst = get_pack_2()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_3():
            lst = get_pack_3()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_5()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_6()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_7():
            lst = get_pack_7()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8():
            lst = get_pack_8()
            VPS.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
    
        
        new_pack_1()
        new_pack_2()
        new_pack_3()
        new_pack_4()
        new_pack_5()
        new_pack_6()
        new_pack_7()
        new_pack_8()
