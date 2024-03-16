from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.services import create_order_from_cart


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        create_order_from_cart(cart_items, user, form)  # Processing order
                        messages.success(request, 'Order is processed!')
                        return redirect('user:profile')

            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Placing an order',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)
