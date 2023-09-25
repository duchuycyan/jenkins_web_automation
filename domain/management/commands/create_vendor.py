from domain.models import Vendor
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create all of vendor'
    

    def add_arguments(self, parser):
        parser.add_argument('-all',action='store_true', help='update_or_create all')

    def handle(self, *args, **kwargs):
        if kwargs['all']:
            Vendor.objects.update_or_create(name='Alibaba Cloud', homepage='https://www.alibabacloud.com/', vendor_location='FOR', logo='icon/alibabacloud.png')
            Vendor.objects.update_or_create(name='AZDIGI', homepage='https://azdigi.com/', vendor_location='VN', logo='icon/azdigi.png')
            Vendor.objects.update_or_create(name='BKHost', homepage='https://bkhost.vn/', vendor_location='VN', logo='icon/bkhost.png')
            Vendor.objects.update_or_create(name='BKNS', homepage='https://www.bkns.vn/', vendor_location='VN', logo='icon/bkns.png')
            Vendor.objects.update_or_create(name='BigRock', homepage='https://www.bigrock.com/', vendor_location='FOR', logo='icon/bigrock.png')
            Vendor.objects.update_or_create(name='ConnectReseller', homepage='https://connectreseller.com/', vendor_location='FOR', logo='icon/connectreseller.png')
            Vendor.objects.update_or_create(name='Crazy Domain', homepage='https://www.crazydomains.com/', vendor_location='FOR', logo='icon/crazy.png')
            Vendor.objects.update_or_create(name='Directnic', homepage='https://directnic.com/', vendor_location='FOR', logo='icon/directnic.png')
            Vendor.objects.update_or_create(name='Domain.com', homepage='https://www.domain.com/', vendor_location='FOR', logo='icon/domain.png')
            Vendor.objects.update_or_create(name='DreamHost', homepage='https://www.dreamhost.com/', vendor_location='FOR', logo='icon/dreamhost.png')
            Vendor.objects.update_or_create(name='Dynadot', homepage='https://www.dynadot.com/', vendor_location='FOR', logo='icon/dynadot.png')
            Vendor.objects.update_or_create(name='ESC', homepage='https://esc.vn/', vendor_location='VN', logo='icon/esc.png')
            Vendor.objects.update_or_create(name='Epik', homepage='https://www.epik.com/', vendor_location='FOR', logo='icon/epik.png')
            Vendor.objects.update_or_create(name='Exabytes', homepage='https://www.exabytes.com/', vendor_location='FOR', logo='icon/exabytes.png')
            Vendor.objects.update_or_create(name='GoDaddy', homepage='https://vn.godaddy.com/', vendor_location='VN', logo='icon/godaddy.png')
            Vendor.objects.update_or_create(name='Google', homepage='https://domains.google/', vendor_location='FOR', logo='icon/google.png')
            Vendor.objects.update_or_create(name='HostVN', homepage='https://hostvn.net/', vendor_location='VN', logo='icon/hostvn.png')
            Vendor.objects.update_or_create(name='HostingViet', homepage='https://hostingviet.vn/', vendor_location='VN', logo='icon/hostingviet.png')
            Vendor.objects.update_or_create(name='Hostinger', homepage='https://www.hostinger.vn/', vendor_location='VN', logo='icon/hostinger.ico')
            Vendor.objects.update_or_create(name='INET', homepage='https://inet.vn/', vendor_location='VN', logo='icon/inet.png')
            Vendor.objects.update_or_create(name='Internet.bs', homepage='https://internetbs.net/', vendor_location='FOR', logo='icon/internetbs.png')
            Vendor.objects.update_or_create(name='MatBao', homepage='https://www.matbao.net/', vendor_location='VN', logo='icon/matbao.png')
            Vendor.objects.update_or_create(name='Name.com', homepage='https://www.name.com/', vendor_location='FOR', logo='icon/name.png')
            Vendor.objects.update_or_create(name='NameBright', homepage='https://www.namebright.com/', vendor_location='FOR', logo='icon/namebright.png')
            Vendor.objects.update_or_create(name='NameHero', homepage='https://www.namehero.com/', vendor_location='FOR', logo='icon/namehero.png')
            Vendor.objects.update_or_create(name='Namecheap', homepage='https://www.namecheap.com/', vendor_location='FOR', logo='icon/namecheap.png')
            Vendor.objects.update_or_create(name='NhanHoa', homepage='https://nhanhoa.com/', vendor_location='VN', logo='icon/nhanhoa.png')
            Vendor.objects.update_or_create(name='P.A VietNam', homepage='https://www.pavietnam.vn/', vendor_location='VN', logo='icon/pavietnam.png')
            Vendor.objects.update_or_create(name='Porkbun', homepage='https://porkbun.com/', vendor_location='FOR', logo='icon/porkbun.png')
            Vendor.objects.update_or_create(name='StableHost', homepage='https://www.stablehost.com/', vendor_location='FOR', logo='icon/stablehost.jpg')
            Vendor.objects.update_or_create(name='TND', homepage='https://www.tnd.vn/', vendor_location='VN', logo='icon/tnd.png')
            Vendor.objects.update_or_create(name='TenTen', homepage='https://tenten.vn/', vendor_location='VN', logo='icon/tenten.png')
            Vendor.objects.update_or_create(name='VHost', homepage='https://vhost.vn/', vendor_location='VN', logo='icon/vhost.png')
            Vendor.objects.update_or_create(name='Viettel IDC', homepage='https://viettelidc.com.vn/', vendor_location='VN', logo='icon/viettelidc.jpg')
            Vendor.objects.update_or_create(name='VinaHost', homepage='https://vinahost.vn/', vendor_location='VN', logo='icon/vinahost.png')
            Vendor.objects.update_or_create(name='Whois.com', homepage='https://www.whois.com/', vendor_location='FOR', logo='icon/whois.png')
            Vendor.objects.update_or_create(name='Z.com', homepage='https://domain.z.com/vn/en/', vendor_location='VN', logo='icon/z.png')
            Vendor.objects.update_or_create(name='NSTech', homepage='https://nstech.vn/', vendor_location='VN', logo='icon/nstech.png')
            # Vendor.objects.update_or_create(name='', homepage='', vendor_location='', logo='')