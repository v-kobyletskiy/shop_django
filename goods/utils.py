from goods.models import Product


def query_search(query):
    if is_id(query):
        return Product.objects.filter(id=int(query))


def is_id(search_param):
    return search_param.isdigit() and len(search_param) <= 5
