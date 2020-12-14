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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from apps.cart.webhook import webhook
from apps.core import views as core_views
from apps.store import views as store_views
from apps.cart import views as cart_views

from apps.coupon.api import api_can_use
from apps.store.api import (
    api_add_to_cart,
    api_remove_from_cart,
    api_checkout,
    create_checkout_session,
)

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'product': ProductSitemap,
    'category': CategorySitemap,
}

urlpatterns = [
    path('', core_views.frontpage, name='frontpage'),
    path('search/', store_views.search, name='search'),
    path('admin/', admin.site.urls),
    path('cart/', cart_views.cart_detail, name='cart'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/', cart_views.success, name='success'),
    path('contact/', core_views.contact, name='contact'),
    path('about/', core_views.about, name='about'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.ciews.sitemap'),

    # API
    path('api/can_use/', api_can_use, name="api_can_use"),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/checkout/', api_checkout, name='api_checkout'),
    # Store
    path('<slug:category_slug>/<slug:slug>/', store_views.product_detail, name='product_detail'),
    path('<slug:slug>/', store_views.category_detail, name='category_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
