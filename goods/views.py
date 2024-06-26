from django.shortcuts import render

from goods.models import Product


# Create your views here.

def catalog(request):
    goods = Product.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context=context)
