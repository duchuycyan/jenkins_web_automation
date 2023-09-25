import requests

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Vendor
from ssl.models import SSL

homepage = "https://nhanhoa.com/"
source = "NhanHoa"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_comodo():
    dom = get_dom('https://nhanhoa.com/ssl-bao-mat/bang-gia-comodo-ssl.html')
    def get_pack_1():
        mark = dom.find('h2', text='Positive SSL').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Positive SSL"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_2():
        mark = dom.find('h2', text='Positive SSL Multi-domain').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Positive SSL Multi-domain"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_3():
        mark = dom.find('h2', text='Positive SSL Wildcard').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Positive SSL Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_4():
        mark = dom.find('h2', text='Comodo EV SSL').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Comodo EV SSL"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_5():
        mark = dom.find('h2', text='Premium SSL Wildcard').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Premium SSL Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_6():
        mark = dom.find('h2', text='Comodo EV Multi Domain SSL').nextSibling.nextSibling
        ssl_type = "comodo"
        pack = "Comodo EV Multi Domain SSL"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[3].text[13:]
        domain_secured = mark.findAll('li')[2].text[25:]
        warranty = mark.findAll('li')[5].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[7].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    return [get_pack_1(), get_pack_2(), get_pack_3(), get_pack_4(), get_pack_5(), get_pack_6()]

def get_geotrust():
    dom = get_dom('https://nhanhoa.com/ssl-bao-mat/bang-gia-geotrust-ssl.html')
    def get_pack_1():
        mark = dom.find('h2', text='Rapid SSL').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "Rapid SSL"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_2():
        mark = dom.find('h2', text='Rapid SSL Wildcard').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "Rapid SSL Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_3():
        mark = dom.find('h2', text='Quick SSL Premium').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "Quick SSL Premium"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_4():
        mark = dom.find('h2', text='QuickSSL Premium Wildcard').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "QuickSSL Premium Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "DV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "standard"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_5():
        mark = dom.find('h2', text='True BusinessID').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "True BusinessID"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_6():
        mark = dom.find('h2', text='True BusinessID Wildcard').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "True BusinessID Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_7():
        mark = dom.find('h2', text='True BusinessID with EV').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "True BusinessID with EV"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_8():
        mark = dom.find('h2', text='True BusinessID Multi-Domain').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "True BusinessID Multi-Domain"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_9():
        mark = dom.find('h2', text='True BusinessID Multi-Domain EV').nextSibling.nextSibling
        ssl_type = "geotrust"
        pack = "True BusinessID Multi-Domain EV"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    return [get_pack_1(), get_pack_2(), get_pack_3(), get_pack_4(), get_pack_5(), get_pack_6(), get_pack_7(), get_pack_8(), get_pack_9()]

def get_symantec():
    dom = get_dom('https://nhanhoa.com/ssl-bao-mat/bang-gia-symantec-ssl.html')
    def get_pack_1():
        mark = dom.find('h2', text='Secure Site').nextSibling.nextSibling
        ssl_type = "symantec"
        pack = "Secure Site"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_2():
        mark = dom.find('h2', text='Secure Site with EV').nextSibling.nextSibling
        ssl_type = "symantec"
        pack = "Secure Site with EV"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_3():
        mark = dom.find('h2', text='Secure Site Wildcard').nextSibling.nextSibling
        ssl_type = "symantec"
        pack = "Secure Site Wildcard"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_4():
        mark = dom.find('h2', text='Secure Site Pro').nextSibling.nextSibling
        ssl_type = "symantec"
        pack = "Secure Site Pro"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "OV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "high"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    def get_pack_5():
        mark = dom.find('h2', text='Secure Site Pro EV').nextSibling.nextSibling
        ssl_type = "symantec"
        pack = "Secure Site Pro EV"
        price = mark.find(class_="price").text.strip().strip(' đ/Năm').replace('.', '')
        validation_type = "EV"
        sans_support = mark.findAll('li')[4].text[13:]
        domain_secured = mark.findAll('li')[3].text[25:]
        warranty = mark.findAll('li')[6].text.strip('Chính sách bảo hiểm: ')
        trust_level = "highest"
        validity_options = mark.findAll('li')[8].text[19:]
        support = "True"
        return [ssl_type, pack, price, validation_type, sans_support, domain_secured, warranty, trust_level, validity_options, support]
    return [get_pack_1(), get_pack_2(), get_pack_3(), get_pack_4(), get_pack_5()]


class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-comodo',action='store_true', help='crawl comodo')
        parser.add_argument('-geotrust',action='store_true', help='crawl geotrust')
        parser.add_argument('-symantec',action='store_true', help='crawl symantec')
        parser.add_argument('-a',action='store_true', help='crawl all')

    
    def handle(self, *args, **kwargs):
        def new_comodo():
            lst = get_comodo()
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Positive SSL', defaults = {'price': lst[0][2], 'validation_type': lst[0][3], 'sans_support': lst[0][4], 'domain_secured': lst[0][5], 'warranty': lst[0][6], 'trust_level': lst[0][7], 'validity_options': lst[0][8], 'support': lst[0][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Positive SSL Multi-domain', defaults = {'price': lst[1][2], 'validation_type': lst[1][3], 'sans_support': lst[1][4], 'domain_secured': lst[1][5], 'warranty': lst[1][6], 'trust_level': lst[1][7], 'validity_options': lst[1][8], 'support': lst[1][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Positive SSL Wildcard', defaults = {'price': lst[2][2], 'validation_type': lst[2][3], 'sans_support': lst[2][4], 'domain_secured': lst[2][5], 'warranty': lst[2][6], 'trust_level': lst[2][7], 'validity_options': lst[2][8], 'support': lst[2][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Comodo EV SSL', defaults = {'price': lst[3][2], 'validation_type': lst[3][3], 'sans_support': lst[3][4], 'domain_secured': lst[3][5], 'warranty': lst[3][6], 'trust_level': lst[3][7], 'validity_options': lst[3][8], 'support': lst[3][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Premium SSL Wildcard', defaults = {'price': lst[4][2], 'validation_type': lst[4][3], 'sans_support': lst[4][4], 'domain_secured': lst[4][5], 'warranty': lst[4][6], 'trust_level': lst[4][7], 'validity_options': lst[4][8], 'support': lst[4][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='comodo', pack='Comodo EV Multi Domain SSL', defaults = {'price': lst[5][2], 'validation_type': lst[5][3], 'sans_support': lst[5][4], 'domain_secured': lst[5][5], 'warranty': lst[5][6], 'trust_level': lst[5][7], 'validity_options': lst[5][8], 'support': lst[5][9]})
        def new_geotrust():
            lst = get_geotrust()
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='Rapid SSL', defaults = {'price': lst[0][2], 'validation_type': lst[0][3], 'sans_support': lst[0][4], 'domain_secured': lst[0][5], 'warranty': lst[0][6], 'trust_level': lst[0][7], 'validity_options': lst[0][8], 'support': lst[0][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='Rapid SSL Wildcard', defaults = {'price': lst[1][2], 'validation_type': lst[1][3], 'sans_support': lst[1][4], 'domain_secured': lst[1][5], 'warranty': lst[1][6], 'trust_level': lst[1][7], 'validity_options': lst[1][8], 'support': lst[1][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='Quick SSL Premium', defaults = {'price': lst[2][2], 'validation_type': lst[2][3], 'sans_support': lst[2][4], 'domain_secured': lst[2][5], 'warranty': lst[2][6], 'trust_level': lst[2][7], 'validity_options': lst[2][8], 'support': lst[2][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='QuickSSL Premium Wildcard', defaults = {'price': lst[3][2], 'validation_type': lst[3][3], 'sans_support': lst[3][4], 'domain_secured': lst[3][5], 'warranty': lst[3][6], 'trust_level': lst[3][7], 'validity_options': lst[3][8], 'support': lst[3][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='True BusinessID', defaults = {'price': lst[4][2], 'validation_type': lst[4][3], 'sans_support': lst[4][4], 'domain_secured': lst[4][5], 'warranty': lst[4][6], 'trust_level': lst[4][7], 'validity_options': lst[4][8], 'support': lst[4][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='True BusinessID Wildcard', defaults = {'price': lst[5][2], 'validation_type': lst[5][3], 'sans_support': lst[5][4], 'domain_secured': lst[5][5], 'warranty': lst[5][6], 'trust_level': lst[5][7], 'validity_options': lst[5][8], 'support': lst[5][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='True BusinessID with EV	', defaults = {'price': lst[6][2], 'validation_type': lst[6][3], 'sans_support': lst[6][4], 'domain_secured': lst[6][5], 'warranty': lst[6][6], 'trust_level': lst[6][7], 'validity_options': lst[6][8], 'support': lst[6][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='True BusinessID Multi-Domain', defaults = {'price': lst[7][2], 'validation_type': lst[7][3], 'sans_support': lst[7][4], 'domain_secured': lst[7][5], 'warranty': lst[7][6], 'trust_level': lst[7][7], 'validity_options': lst[7][8], 'support': lst[7][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='geotrust', pack='True BusinessID Multi-Domain EV', defaults = {'price': lst[8][2], 'validation_type': lst[8][3], 'sans_support': lst[8][4], 'domain_secured': lst[8][5], 'warranty': lst[8][6], 'trust_level': lst[8][7], 'validity_options': lst[8][8], 'support': lst[8][9]})
        def new_symantec():
            lst = get_symantec()
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='symantec', pack='Secure Site', defaults = {'price': lst[0][2], 'validation_type': lst[0][3], 'sans_support': lst[0][4], 'domain_secured': lst[0][5], 'warranty': lst[0][6], 'trust_level': lst[0][7], 'validity_options': lst[0][8], 'support': lst[0][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='symantec', pack='Secure Site with EV', defaults = {'price': lst[1][2], 'validation_type': lst[1][3], 'sans_support': lst[1][4], 'domain_secured': lst[1][5], 'warranty': lst[1][6], 'trust_level': lst[1][7], 'validity_options': lst[1][8], 'support': lst[1][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='symantec', pack='Secure Site Wildcard', defaults = {'price': lst[2][2], 'validation_type': lst[2][3], 'sans_support': lst[2][4], 'domain_secured': lst[2][5], 'warranty': lst[2][6], 'trust_level': lst[2][7], 'validity_options': lst[2][8], 'support': lst[2][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='symantec', pack='Secure Site Pro', defaults = {'price': lst[3][2], 'validation_type': lst[3][3], 'sans_support': lst[3][4], 'domain_secured': lst[3][5], 'warranty': lst[3][6], 'trust_level': lst[3][7], 'validity_options': lst[3][8], 'support': lst[3][9]})
            SSL.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), ssl_type='symantec', pack='Secure Site Pro EV', defaults = {'price': lst[4][2], 'validation_type': lst[4][3], 'sans_support': lst[4][4], 'domain_secured': lst[4][5], 'warranty': lst[4][6], 'trust_level': lst[4][7], 'validity_options': lst[4][8], 'support': lst[4][9]})
        if kwargs['comodo']:
            new_comodo()
        elif kwargs['geotrust']:
            new_geotrust()
        elif kwargs['symantec']:
            new_symantec()
        elif kwargs['a']:
            new_comodo()
            new_geotrust()
            new_symantec()
        else:
            print("Invalid options! Please type '-h' for help")
        