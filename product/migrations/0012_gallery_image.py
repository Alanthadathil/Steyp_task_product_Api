# Generated by Django 4.1.2 on 2022-10-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_product_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='a', upload_to='products/media/images'),
            preserve_default=False,
        ),
    ]
