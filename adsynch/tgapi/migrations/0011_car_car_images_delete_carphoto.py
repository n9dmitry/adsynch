# Generated by Django 5.0.4 on 2024-04-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0010_remove_car_image_carphoto_delete_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_images',
            field=models.ImageField(default='JPG', max_length=10, upload_to='static/media'),
        ),
        migrations.DeleteModel(
            name='CarPhoto',
        ),
    ]