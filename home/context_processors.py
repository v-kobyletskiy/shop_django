from goods.models import ProductCategory


def goods_categories(request):
    return {
        'categories': ProductCategory.objects.filter(is_visible=True).order_by('position'),
    }
