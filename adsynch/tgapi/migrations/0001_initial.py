# Generated by Django 4.0.6 on 2024-04-24 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RealtyAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.CharField(default='0', max_length=100)),
                ('photos', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(default='0', max_length=255)),
                ('contact_name', models.CharField(default='0', max_length=255)),
                ('contact_phone', models.CharField(default='0', max_length=20)),
                ('description', models.TextField(default='0')),
                ('currency', models.CharField(default='0', max_length=5)),
                ('price', models.IntegerField()),
                ('rooms_number', models.IntegerField()),
                ('realty_deal', models.CharField(default='0', max_length=100)),
                ('realty_type', models.CharField(default='0', max_length=100)),
                ('realty_square', models.FloatField()),
                ('realty_rooms', models.CharField(default='0', max_length=100)),
                ('realty_floor', models.IntegerField()),
                ('realty_floors_total', models.IntegerField()),
                ('realty_currency', models.CharField(default='0', max_length=255)),
                ('realty_price', models.FloatField()),
                ('realty_contacts', models.CharField(default='0', max_length=255)),
                ('realty_name', models.CharField(default='0', max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.CharField(default='0', max_length=100)),
                ('photos', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(default='0', max_length=255)),
                ('contact_name', models.CharField(default='0', max_length=255)),
                ('contact_phone', models.CharField(default='0', max_length=20)),
                ('description', models.TextField(default='0')),
                ('currency', models.CharField(default='0', max_length=5)),
                ('price', models.IntegerField()),
                ('job_title', models.CharField(default='0', max_length=255)),
                ('job_requirements', models.TextField()),
                ('job_responsibilities', models.TextField()),
                ('job_conditions', models.TextField()),
                ('job_currency', models.CharField(default='0', max_length=255)),
                ('job_price', models.FloatField(default='0')),
                ('job_contacts', models.CharField(default='0', max_length=255)),
                ('job_name', models.CharField(default='0', max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.CharField(default='0', max_length=100)),
                ('photos', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(default='0', max_length=255)),
                ('contact_name', models.CharField(default='0', max_length=255)),
                ('contact_phone', models.CharField(default='0', max_length=20)),
                ('description', models.TextField(default='0')),
                ('currency', models.CharField(default='0', max_length=5)),
                ('price', models.IntegerField()),
                ('car_brand', models.CharField(default='0', max_length=255)),
                ('car_model', models.CharField(default='0', max_length=255)),
                ('car_year', models.IntegerField()),
                ('car_body_type', models.CharField(default='0', max_length=255)),
                ('car_engine_type', models.CharField(default='0', max_length=255)),
                ('car_engine_volume', models.CharField(default='0', max_length=255)),
                ('car_power', models.CharField(default='0', max_length=255)),
                ('car_transmission_type', models.CharField(default='0', max_length=255)),
                ('car_color', models.CharField(default='0', max_length=255)),
                ('car_mileage', models.TextField()),
                ('car_document_status', models.CharField(default='0', max_length=255)),
                ('car_owners', models.TextField()),
                ('car_customs_cleared', models.TextField()),
                ('car_condition', models.CharField(default='0', max_length=255)),
                ('car_description', models.TextField()),
                ('car_currency', models.CharField(default='0', max_length=255)),
                ('car_price', models.FloatField(default='0')),
                ('car_location', models.CharField(default='0', max_length=255)),
                ('seller_name', models.CharField(default='0', max_length=255)),
                ('seller_phone', models.CharField(default='0', max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
