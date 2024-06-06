from users.models import User
from django.db import models

from goods.models import Product


# Create your models here.
class CartQuerySet(models.query.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'CART {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
        return f'Anonymous cart | Product {self.product.name} | Quantity {self.quantity}'
