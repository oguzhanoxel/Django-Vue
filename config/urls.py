"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.core import views as core_views
from apps.store import views as store_views
from apps.cart import views as cart_views

urlpatterns = [
    path('', core_views.frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('cart/', cart_views.cart, name='cart'),
    path('contact/', core_views.contact, name='contact'),
    path('about/', core_views.about, name='about'),
    path('<slug:category_slug>/<slug:slug>/', store_views.product_detail, name='product_detail'),
    path('<slug:slug>/', store_views.category_detail, name='category_detail'),
]
