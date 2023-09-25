import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.hostinger.vn/"
urls = "https://www.hostinger.vn/kiem-tra-ten-mien-gia-re"
source = "Hostinger"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"src": "//www.hostinger.vn/assets/images/domain-checker/icon-com-8a6804da47.svg"})
    mark_origin_parent = mark_origin.parent
    reg_origin = mark_origin_parent.contents[3].contents[1].contents[0].text.strip('VNĐ/năm').strip().replace('.', '')
    reg_promotion = reg_origin
    return [reg_origin, reg_promotion]


class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-a',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Hostinger'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        if kwargs['com']:
            new_com()
        elif kwargs['a']:
            new_com()
        else:
            print("Invalid options! Please type '-h' for help")