# Generated by Django 5.0.4 on 2024-04-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0011_car_car_images_delete_carphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_images',
        ),
        migrations.AddField(
            model_name='car',
            name='photo_urls',
            field=models.TextField(blank=True, null=True),
        ),
    ]