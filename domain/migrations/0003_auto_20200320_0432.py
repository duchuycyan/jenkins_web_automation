# Generated by Django 2.1.15 on 2020-03-20 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domain', '0002_auto_20200320_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_type', models.CharField(choices=[('vn', '.vn'), ('com', '.com'), ('comvn', '.com.vn'), ('net', '.net'), ('org', '.org'), ('info', '.info')], default='vn', max_length=10)),
                ('reg_origin', models.IntegerField(null=True)),
                ('reg_origin_usd', models.CharField(blank=True, max_length=10)),
                ('reg_promotion', models.IntegerField(null=True)),
                ('reg_promotion_usd', models.CharField(blank=True, max_length=10)),
                ('renew_price', models.IntegerField(null=True)),
                ('renew_price_usd', models.CharField(blank=True, max_length=10)),
                ('trans_price', models.IntegerField(null=True)),
                ('trans_price_usd', models.CharField(blank=True, max_length=10)),
                ('rates', models.CharField(blank=True, max_length=10)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('homepage', models.CharField(max_length=30, unique=True)),
                ('vendor_location', models.CharField(choices=[('FOR', 'Foreign'), ('VN', 'VietNam')], default='VN', max_length=10)),
                ('logo', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Vendor'),
        ),
    ]
