from django.urls import path, include
from . import views
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('blank/', views.blank, name='blank'),
    path('product/', views.product, name='product'),
    path('', views.store, name='store')
    ]

