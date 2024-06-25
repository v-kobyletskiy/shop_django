from django import template

from goods.models import ProductCategory

register = template.Library()

@register.simple_tag()
def tag_categories():
    # return ProductCategory.objects.filter(is_visible=True).order_by('position'),
    return ProductCategory.objects.all(),
