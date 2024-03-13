from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products


def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(1)

    context = {
        'title': 'Fucking shop - Catalog',
        'goods': current_page,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    current_product = Products.objects.get(slug=product_slug)
    context = {
        'product': current_product
    }
    return render(request, 'goods/product.html', context)
