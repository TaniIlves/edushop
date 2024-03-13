from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Fucking shop - Catalog',
        'goods': goods,
     }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    current_product = Products.objects.get(slug=product_slug)
    context = {
        'product': current_product
    }
    return render(request, 'goods/product.html', context)
