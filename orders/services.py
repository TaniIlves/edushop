from django.core.exceptions import ValidationError

from orders.models import Order, OrderItem


def create_order_from_cart(cart_items, user, form):
    order = Order.objects.create(
        user=user,
        phone_number=form.cleaned_data['phone_number'],
        requires_delivery=form.cleaned_data['requires_delivery'],
        delivery_address=form.cleaned_data['delivery_address'],
        payment_on_get=form.cleaned_data['payment_on_get'],
    )

    # Create ordered products
    for cart_item in cart_items:
        product = cart_item.product
        name = cart_item.product.name
        price = cart_item.product.sell_price()
        quantity = cart_item.quantity

        if product.quantity < quantity:
            raise ValidationError(
                f'Not enough items {name} in store. In stock: {product.quantity}'
            )

        OrderItem.objects.create(
            order=order,
            product=product,
            name=name,
            price=price,
            quantity=quantity,
        )
        product.quantity -= quantity
        product.save()

    # Empty the user's cart after creating an order
    cart_items.delete()