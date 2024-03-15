from django.db import models

from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='User',
    )
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Good')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Order added date')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects = CartQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f'User: {self.user.username}, Item: "{self.product.name}", qty: {self.quantity}'
        return f'Anonymous cart, Item: {self.product.name}, qty: {self.quantity}'

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

# For future
# order_id = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Order #')
#
# class Order(models.Model):
#     cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, verbose_name='Cart')
