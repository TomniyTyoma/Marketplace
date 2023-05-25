from django.urls import path, include
from . import views
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.blank, name='cart'),
    path('product/', views.product, name='product'),
    path('', views.ProductsListView.as_view(), name='store')
    ]

