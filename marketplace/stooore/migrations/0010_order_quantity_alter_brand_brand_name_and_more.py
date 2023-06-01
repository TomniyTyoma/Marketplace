# Generated by Django 4.1.7 on 2023-05-31 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stooore', '0009_alter_product_char'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=30, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=30, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_best_offer',
            field=models.BooleanField(default=False, verbose_name='Лучшее предложение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
