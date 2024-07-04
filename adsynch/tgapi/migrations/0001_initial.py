# Generated by Django 5.0.4 on 2024-07-02 09:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_tg', models.CharField(blank=True, max_length=100, null=True)),
                ('ad_id', models.CharField(blank=True, max_length=100, null=True)),
                ('photos', models.TextField(blank=True, null=True)),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=5, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
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
                ('car_price', models.FloatField(default='0')),
                ('car_location', models.CharField(default='0', max_length=255)),
                ('car_name', models.CharField(default='0', max_length=255)),
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
                ('username_tg', models.CharField(blank=True, max_length=100, null=True)),
                ('ad_id', models.CharField(blank=True, max_length=100, null=True)),
                ('photos', models.TextField(blank=True, null=True)),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=5, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('job_category', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RealtyAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_tg', models.CharField(blank=True, max_length=100, null=True)),
                ('ad_id', models.CharField(blank=True, max_length=100, null=True)),
                ('photos', models.TextField(blank=True, null=True)),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=5, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('realty_deal', models.CharField(blank=True, max_length=100, null=True)),
                ('realty_type', models.CharField(blank=True, max_length=100, null=True)),
                ('realty_commercial_type', models.CharField(blank=True, max_length=100, null=True)),
                ('realty_square', models.FloatField(blank=True, null=True)),
                ('realty_location', models.CharField(blank=True, max_length=255, null=True)),
                ('realty_rooms', models.IntegerField(blank=True, null=True)),
                ('realty_floor', models.IntegerField(blank=True, null=True)),
                ('realty_floors_total', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
