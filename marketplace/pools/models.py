from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.TextField(blank=True, null=True)

