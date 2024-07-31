from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator

from goods.models import Product
from goods.utils import query_search

CATEGORY_ALL = 'all'


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    on_sale = request.GET.get('on_sale', None)
    query = request.GET.get('q', None)

    if category_slug == CATEGORY_ALL:
        goods = Product.objects.all()
    elif query:
        goods = query_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404()
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

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
    return render(request, 'product.html', context)
