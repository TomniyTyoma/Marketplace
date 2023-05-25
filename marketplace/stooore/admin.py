from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Brand, Category, Product, Order, OrderItem, Profile, Review

admin.site.unregister(User)


class UserActivitiesInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    inlines = [UserActivitiesInline]


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
