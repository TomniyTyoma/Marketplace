# Generated by Django 4.1.7 on 2023-05-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stooore', '0003_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
