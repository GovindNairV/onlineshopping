# Generated by Django 4.0.4 on 2022-05-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_merge_20220509_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='streetaddress',
        ),
        migrations.AddField(
            model_name='address',
            name='AddressLine1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
