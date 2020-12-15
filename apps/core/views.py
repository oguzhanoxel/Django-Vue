from django.shortcuts import render

from apps.store.models import Product
# from apps.order.models import Order


# def order_confirmation(request):
#     order = Order.objects.get(pk=13)
#     return render(request, 'order_confirmation.html', {'order': order})


def frontpage(request):
    products = Product.objects.filter(is_featured=True)
    context = {
        'products': products,
    }
    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
