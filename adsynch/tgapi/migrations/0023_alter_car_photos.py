# Generated by Django 5.0.4 on 2024-04-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0022_alter_car_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photos',
            field=models.TextField(blank=True),
        ),
    ]
