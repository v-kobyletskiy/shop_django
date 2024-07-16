from django.db import models

from goods.models import Product
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum([cart.products_price() for cart in self])

    def total_count(self):
        if self:
            return sum([cart.quantity for cart in self])
        return 0


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart | {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    class Meta:
        verbose_name_plural = "Cart"

    objects = CartQueryset.as_manager()
