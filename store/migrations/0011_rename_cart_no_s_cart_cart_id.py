# Generated by Django 4.0.4 on 2022-05-08 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_s_cart_cart_id_s_cart_cart_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='s_cart',
            old_name='cart_no',
            new_name='cart_id',
        ),
    ]