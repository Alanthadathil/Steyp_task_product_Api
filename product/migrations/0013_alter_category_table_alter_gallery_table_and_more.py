# Generated by Django 4.1.2 on 2022-10-18 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_gallery_image'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='products_category',
        ),
        migrations.AlterModelTable(
            name='gallery',
            table='products_gallery',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products_product',
        ),
    ]
