# Generated by Django 4.0.4 on 2022-05-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_s_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s_cart',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='s_cart',
            name='cart_no',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
