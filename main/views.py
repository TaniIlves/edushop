from django.shortcuts import render
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()


    context = {
        'title': 'Fucking shop - Main',
        'content': 'Home page of the Fucking shop',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Fucking shop - About',
        'content': 'About the Fucking shop',
        'text_on_page': 'The Fucking shop is the best fucking shop in the fucking world'
    }

    return render(request, 'main/about.html', context)
