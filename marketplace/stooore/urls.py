from django.urls import path, include
from . import views
urlpatterns = [
    path('checkout/', views.make_order, name='checkout'),
    path('cart/', views.cart_view, name='cart'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('', views.ProductsListView.as_view(), name='store'),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    ]

