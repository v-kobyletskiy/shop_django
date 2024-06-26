from goods.models import ProductCategory


def goods_categories(request):
    # return ProductCategory.objects.filter(is_visible=True).order_by('position'),
    return {
        'categories': ProductCategory.objects.all(),
    }
