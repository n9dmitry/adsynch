# Generated by Django 5.0.4 on 2024-05-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0002_userprofilelink_rename_car_currency_carad_car_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobad',
            name='job_category',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
