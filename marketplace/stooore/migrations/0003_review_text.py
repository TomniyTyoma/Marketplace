# Generated by Django 4.1.7 on 2023-05-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stooore', '0002_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
