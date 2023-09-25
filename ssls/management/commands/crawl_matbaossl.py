import requests

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from ssl.models import SSL

homepage = "https://www.matbao.net/"
source = "MatBao"


def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_geotrust():
    dom = get_dom('https://www.matbao.net/bao-mat-website/geotrust-ssl.html')
    def get_pack_1():
        ssl_type = "geotrust"
        pack = "Rapid SSL"
        price = dom.find(attrs={'id': 'div_HP20070907103142_PhiDuyTri'}).string.replace('.', '')
        validation_type = "DV"
        sans_support = "Không"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[3].string
        trust_level = "standard"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[3].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_2():
        ssl_type = "geotrust"
        pack = "Rapid SSL Wildcard"
        price = dom.find(attrs={'id': 'div_HP20070907104342_PhiDuyTri'}).string.replace('.', '')
        validation_type = "DV"
        sans_support = "Không"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[5].string
        trust_level = "standard"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[5].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_3():
        ssl_type = "geotrust"
        pack = "Quick SSL Premium"
        price = dom.find(attrs={'id': 'div_HP20160525150132_PhiDuyTri'}).string.replace('.', '')
        validation_type = "DV"
        sans_support = "Không"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[7].string
        trust_level = "standard"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[7].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_5():
        ssl_type = "geotrust"
        pack = "True BusinessID"
        price = dom.find(attrs={'id': 'div_HP20070907106342_PhiDuyTri'}).string.replace('.', '')
        validation_type = "OV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[9].string
        trust_level = "high"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[9].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_6():
        ssl_type = "geotrust"
        pack = "True BusinessID Wildcard"
        price = dom.find(attrs={'id': 'div_HP20070907104642_PhiDuyTri'}).string.replace('.', '')
        validation_type = "OV"
        sans_support = "Không"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[11].string
        trust_level = "high"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[11].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_7():
        ssl_type = "geotrust"
        pack = "True BusinessID with EV"
        price = dom.find(attrs={'id': 'div_HP20160525150135_PhiDuyTri'}).string.replace('.', '')
        validation_type = "EV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[13].string
        trust_level = "highest"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[13].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    return [get_pack_1(), get_pack_2(), get_pack_3(), get_pack_5(), get_pack_6(), get_pack_7()]

def get_symantec():
    dom = get_dom('https://www.matbao.net/bao-mat-website/symantec-ssl.html')
    def get_pack_1():
        ssl_type = "symantec"
        pack = "Secure Site"
        price = dom.find(attrs={'id': 'div_HP20155607035622_PhiDuyTri'}).string.replace('.', '')
        validation_type = "OV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[11].string
        trust_level = "high"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[11].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    def get_pack_2():
        ssl_type = "symantec"
        pack = "Secure Site with EV"
        price = dom.find(attrs={'id': 'div_HP20150107040101_PhiDuyTri'}).string.replace('.', '')
        validation_type = "EV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[9].string
        trust_level = "highest"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[9].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]

    def get_pack_3():
        ssl_type = "symantec"
        pack = "Secure Site Wildcard"
        price = dom.find(attrs={'id': 'div_HP20160525150145_PhiDuyTri'}).string.replace('.', '')
        validation_type = "OV"
        sans_support = "Không"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[7].string
        trust_level = "high"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[7].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]

    def get_pack_4():
        ssl_type = "symantec"
        pack = "Secure Site Pro"
        price = dom.find(attrs={'id': 'div_HP20155807035830_PhiDuyTri'}).string.replace('.', '')
        validation_type = "OV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[5].string
        trust_level = "high"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[5].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]

    def get_pack_5():
        ssl_type = "symantec"
        pack = "Secure Site Pro EV"
        price = dom.find(attrs={'id': 'div_HP20150307040357_PhiDuyTri'}).string.replace('.', '')
        validation_type = "EV"
        sans_support = "Có"
        domain_secured = dom.find('td', text='Số domain được bảo mật').parent.contents[11].string
        trust_level = "highest"
        validity_options = dom.find('td', text='Cho phép đăng ký').parent.contents[11].string
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, trust_level, validity_options, support]
    return [get_pack_1(), get_pack_2(), get_pack_3(), get_pack_4(), get_pack_5()]


class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-comodo',action='store_true', help='crawl comodo')
        parser.add_argument('-geotrust',action='store_true', help='crawl geotrust')
        parser.add_argument('-symantec',action='store_true', help='crawl symantec')
        parser.add_argument('-a',action='store_true', help='crawl all')

    
    def handle(self, *args, **kwargs):
        def new_geotrust():
            lst = get_geotrust()
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='Rapid SSL', defaults = {'price': lst[0][2], 'validation_type': lst[0][3], 'sans_support': lst[0][4], 'domain_secured': lst[0][5], 'trust_level': lst[0][6], 'validity_options': lst[0][7], 'support': lst[0][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='Rapid SSL Wildcard', defaults = {'price': lst[1][2], 'validation_type': lst[1][3], 'sans_support': lst[1][4], 'domain_secured': lst[1][5], 'trust_level': lst[1][6], 'validity_options': lst[1][7], 'support': lst[1][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='Quick SSL Premium', defaults = {'price': lst[2][2], 'validation_type': lst[2][3], 'sans_support': lst[2][4], 'domain_secured': lst[2][5], 'trust_level': lst[2][6], 'validity_options': lst[2][7], 'support': lst[2][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='True BusinessID', defaults = {'price': lst[3][2], 'validation_type': lst[3][3], 'sans_support': lst[3][4], 'domain_secured': lst[3][5], 'trust_level': lst[3][6], 'validity_options': lst[3][7], 'support': lst[3][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='True BusinessID Wildcard', defaults = {'price': lst[4][2], 'validation_type': lst[4][3], 'sans_support': lst[4][4], 'domain_secured': lst[4][5], 'trust_level': lst[4][6], 'validity_options': lst[4][7], 'support': lst[4][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='geotrust', pack='True BusinessID with EV	', defaults = {'price': lst[5][2], 'validation_type': lst[5][3], 'sans_support': lst[5][4], 'domain_secured': lst[5][5], 'trust_level': lst[5][6], 'validity_options': lst[5][7], 'support': lst[5][8]})

        def new_symantec():
            lst = get_symantec()
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='symantec', pack='Secure Site', defaults = {'price': lst[0][2], 'validation_type': lst[0][3], 'sans_support': lst[0][4], 'domain_secured': lst[0][5], 'trust_level': lst[0][6], 'validity_options': lst[0][7], 'support': lst[0][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='symantec', pack='Secure Site with EV', defaults = {'price': lst[1][2], 'validation_type': lst[1][3], 'sans_support': lst[1][4], 'domain_secured': lst[1][5], 'trust_level': lst[1][6], 'validity_options': lst[1][7], 'support': lst[1][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='symantec', pack='Secure Site Wildcard', defaults = {'price': lst[2][2], 'validation_type': lst[2][3], 'sans_support': lst[2][4], 'domain_secured': lst[2][5], 'trust_level': lst[2][6], 'validity_options': lst[2][7], 'support': lst[2][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='symantec', pack='Secure Site Pro', defaults = {'price': lst[3][2], 'validation_type': lst[3][3], 'sans_support': lst[3][4], 'domain_secured': lst[3][5], 'trust_level': lst[3][6], 'validity_options': lst[3][7], 'support': lst[3][8]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), ssl_type='symantec', pack='Secure Site Pro EV', defaults = {'price': lst[4][2], 'validation_type': lst[4][3], 'sans_support': lst[4][4], 'domain_secured': lst[4][5], 'trust_level': lst[4][6], 'validity_options': lst[4][7], 'support': lst[4][8]})
        if kwargs['geotrust']:
            new_geotrust()
        elif kwargs['symantec']:
            new_symantec()
        elif kwargs['a']:
            new_geotrust()
            new_symantec()
        else:
            print("Invalid options! Please type '-h' for help")