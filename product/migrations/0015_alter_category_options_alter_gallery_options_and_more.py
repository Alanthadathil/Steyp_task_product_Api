# Generated by Django 4.1.2 on 2022-10-19 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_category_image_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'gallery'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'products'},
        ),
    ]
