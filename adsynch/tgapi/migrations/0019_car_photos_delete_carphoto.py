# Generated by Django 5.0.4 on 2024-04-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0018_remove_car_photos_carphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photos',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CarPhoto',
        ),
    ]