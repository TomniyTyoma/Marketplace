from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.brand_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.product_name} - {self.price}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Review(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user} - {self.product} - {self.rating}'


class Order(models.Model):
    STATUS_CART = '1_cart'
    STATUS_WAITING_FOR_PAYMENT = '2_waiting_for_payment'
    STATUS_PAID = '3_paid'
    STATUS_CHOICES = [
        (STATUS_CART, 'cart'),
        (STATUS_WAITING_FOR_PAYMENT, 'waiting_for_payment'),
        (STATUS_PAID, 'paid')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default=STATUS_CART)
    comment = models.TextField()
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.product} - {self.price} - {self.quantity}'
