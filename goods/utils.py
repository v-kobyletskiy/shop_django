from django.db.models import Q
from goods.models import Product


def query_search(query):
    if is_id(query):
        return Product.objects.filter(id=int(query))
    keywords = [word for word in query.split() if len(word) > 3]

    queries = Q()

    for keyword in keywords:
        queries |= Q(name__icontains=keyword)
        queries |= Q(description__icontains=keyword)
    return Product.objects.filter(queries)


def is_id(search_param):
    return search_param.isdigit() and len(search_param) <= 5
