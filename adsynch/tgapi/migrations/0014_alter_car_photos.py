# Generated by Django 5.0.4 on 2024-04-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0013_rename_photo_urls_car_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='cars'),
        ),
    ]