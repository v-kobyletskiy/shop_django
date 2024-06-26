from django.shortcuts import get_object_or_404, render

from goods.models import Product

CATEGORY_ALL = 'all'

# Create your views here.

def catalog(request, category_slug):
    if category_slug == CATEGORY_ALL:
        goods = Product.objects.all()
    else:
        goods = Product.objects.filter(category__slug=category_slug)
        # goods = get_object_or_404(Product.objects.filter(category__slug=category_slug))

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
