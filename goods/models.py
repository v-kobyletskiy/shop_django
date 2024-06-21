from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Product Categories'

class Product(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='products/', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    quantity = models.PositiveSmallIntegerField(default=0)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Products'
