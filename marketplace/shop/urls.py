
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('blank/', views.blank, name='blank'),
    path('product/', views.product, name='product'),
    path('auth/', include('authentication.urls')),
]
