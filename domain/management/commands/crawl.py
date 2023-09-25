import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Crawl All of PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-all',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        if kwargs['all']:
            try:
                os.system("python manage.py crawl_nhanhoa -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_alibaba -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_azdigi -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_bigrock -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_bkhost -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_bkns -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_crazy -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_directnic -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_domaincom -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_dreamhost -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_dynadot -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_epik -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_esc -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_exabytes -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_godaddy -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_google -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_hostinger -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_hostingviet -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_hostvn -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_inet -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_internetbs -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_matbao -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_namebright -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_namecheap -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_namecom -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_namehero -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_pa -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_porkbun -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_reseller -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_stablehost -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_tenten -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_tnd -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_vhost -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_viettel -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_vinahost -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_whois -a")
            except Exception as error:
                print(error)
            try:
                os.system("python manage.py crawl_zcom -a")
            except Exception as error:
                print(error)
        else:
            print("Invalid options! Please type '-h' for help")