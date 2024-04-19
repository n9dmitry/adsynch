# Generated by Django 5.0.4 on 2024-04-09 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0009_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.URLField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='tgapi.car')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]