from django.contrib import admin
from django.utils.safestring import mark_safe
from goods.models import ProductCategory, Product

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('photo_src_tag', 'name', 'slug', 'description', 'photo', 'price', 'photo', 'price', 'discount',
                    'quantity', 'position', 'is_visible', 'category')
    list_editable = ('name', 'position', 'is_visible', 'category')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Product photo'
