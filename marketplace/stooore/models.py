from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone


class Brand(models.Model):
    brand_name = models.CharField('Бренд', max_length=30)

    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f'{self.brand_name}'


class Category(models.Model):
    category_name = models.CharField('Категория', max_length=30)

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField('Название', max_length=150)
    price = models.DecimalField('Цена', max_digits=19, decimal_places=2)
    description = models.TextField('Описание', blank=True, null=True)
    char = models.TextField('Характеристики', default='')
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField('Изображение', blank=True, null=True)
    availability = models.BooleanField(default=True)
    is_best_offer = models.BooleanField('Лучшее предложение', default=False)

    class Meta:
        ordering = ['availability', '-category_id', 'price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.product_name}'


class OtherImgs(models.Model):
    img_urls = models.URLField(blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['product_id']
        verbose_name = 'Другие изображения товара'
        verbose_name_plural = 'Другие изображения товаров'


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
    text = models.TextField(default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

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
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.status}'

    @staticmethod
    def get_cart(user: User):
        cart = Order.objects.filter(user=user, status=Order.STATUS_CART).first()

        if cart and (timezone.now() - cart.creation_time).days > 7:
            cart.delete()
            cart = None

        if not cart:
            cart = Order.objects.create(user=user, status=Order.STATUS_CART, amount=0)

        return cart

    def get_amount(self):
        amount = Decimal(0)
        for item in self.orderitem_set.all():
            amount += item.amount
        return amount

    def get_quantity(self):
        quantity = Decimal(0)
        for item in self.orderitem_set.all():
            quantity += item.quantity
        return quantity

    def make_order(self):
        items = self.orderitem_set.all()
        if items and self.status == Order.STATUS_CART:
            self.status = Order.STATUS_WAITING_FOR_PAYMENT
            self.save()

    @staticmethod
    def get_amount_of_unpaid_orders(user: User):
        amount = Order.objects.filter(user=user, status=Order.STATUS_WAITING_FOR_PAYMENT, ).aggregate(Sum('amount'))[
            'amount__sum']
        return amount or Decimal(0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return f'{self.product} - {self.price} - {self.quantity}'

    @property
    def amount(self):
        return self.quantity * (self.price - self.discount)


@receiver(post_save, sender=OrderItem)
def recalculate_order_amount_after_save(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()


@receiver(post_delete, sender=OrderItem)
def recalculate_order_amount_after_delete(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()
