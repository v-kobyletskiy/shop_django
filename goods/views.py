from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Product

CATEGORY_ALL = 'all'

# Create your views here.

def catalog(request, category_slug, page=1):
    if category_slug == CATEGORY_ALL:
        goods = Product.objects.all()
    else:
        # goods = Product.objects.filter(category__slug=category_slug)
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context=context)
