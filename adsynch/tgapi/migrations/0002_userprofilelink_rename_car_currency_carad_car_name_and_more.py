# Generated by Django 5.0.4 on 2024-05-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapi', '0001_initial'),
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
        migrations.RenameField(
            model_name='carad',
            old_name='car_currency',
            new_name='car_name',
        ),
        migrations.RemoveField(
            model_name='carad',
            name='car_description',
        ),
        migrations.RemoveField(
            model_name='carad',
            name='seller_name',
        ),
        migrations.RemoveField(
            model_name='carad',
            name='seller_phone',
        ),
        migrations.RemoveField(
            model_name='jobad',
            name='job_contacts',
        ),
        migrations.RemoveField(
            model_name='jobad',
            name='job_currency',
        ),
        migrations.RemoveField(
            model_name='jobad',
            name='job_description',
        ),
        migrations.RemoveField(
            model_name='jobad',
            name='job_name',
        ),
        migrations.RemoveField(
            model_name='jobad',
            name='job_price',
        ),
        migrations.RemoveField(
            model_name='realtyad',
            name='realty_contacts',
        ),
        migrations.RemoveField(
            model_name='realtyad',
            name='realty_currency',
        ),
        migrations.RemoveField(
            model_name='realtyad',
            name='realty_name',
        ),
        migrations.RemoveField(
            model_name='realtyad',
            name='realty_price',
        ),
        migrations.AddField(
            model_name='carad',
            name='category',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='carad',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='jobad',
            name='category',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='jobad',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='realtyad',
            name='category',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='realtyad',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
