# Generated by Django 4.1.2 on 2022-10-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_categorylist_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]