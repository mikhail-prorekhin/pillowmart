# Generated by Django 5.2.4 on 2025-07-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='big_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='products_images', verbose_name='Big Image 1'),
        ),
        migrations.AddField(
            model_name='products',
            name='big_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='products_images', verbose_name='Big Image 2'),
        ),
        migrations.AddField(
            model_name='products',
            name='big_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='products_images', verbose_name='Big Image 3'),
        ),
        migrations.AddField(
            model_name='products',
            name='full_description',
            field=models.TextField(blank=True, null=True, verbose_name='Full Description'),
        ),
    ]
