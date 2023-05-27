
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductsListView.as_view(), name='home'),
    path('store/', include('stooore.urls')),
    path('auth/', include('authentication.urls')),

]
