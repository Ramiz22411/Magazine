from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Category, Product
from django.core.paginator import Paginator
from .utils import q_search


# Create your views here.

def catalog(request, category_slug=None):
    query = request.GET.get('q', None)
    page = request.GET.get('page', 1)

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    template = 'goods/catalog.html'
    context = {
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, template, context)


def product(request, product_slug):
    template = 'goods/product.html'
    context = {
        "product": get_object_or_404(Product, slug=product_slug)
    }
    return render(request, template, context)
