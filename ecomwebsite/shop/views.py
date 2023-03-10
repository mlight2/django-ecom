from turtle import title
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Products

def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')

    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_objects = Products.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_objects': product_objects})
