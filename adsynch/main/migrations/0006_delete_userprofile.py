# Generated by Django 5.0.4 on 2024-07-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userprofile_username_tg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
