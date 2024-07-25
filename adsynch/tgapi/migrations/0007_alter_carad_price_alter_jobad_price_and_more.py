# Generated by Django 5.0.4 on 2024-07-25 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0006_alter_carad_price_alter_jobad_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carad',
            name='price',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(message='Price must be an integer', regex='^\\d+$')]),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='price',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(message='Price must be an integer', regex='^\\d+$')]),
        ),
        migrations.AlterField(
            model_name='realtyad',
            name='price',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(message='Price must be an integer', regex='^\\d+$')]),
        ),
    ]
