# Generated by Django 4.1.7 on 2023-05-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stooore', '0006_otherimgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_best_offer',
            field=models.BooleanField(default=False),
        ),
    ]
