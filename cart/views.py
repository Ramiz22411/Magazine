from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from goods.models import Product

from .models import Cart
from .utils import get_user_carts


# Create your views here.


def cart_add(request):
    product_id = request.POST['product_id']
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'include_cart.html', {'carts': user_cart}, request=request
    )

    response_data = {
        'message': 'You have successfully added',
        'cart_items_html': cart_items_html,

    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'include_cart.html', {'carts': cart}, request=request
    )
    response_data = {
        'message': 'Quantity changed',
        'cart_items_html': cart_items_html,
        'quantity': updated_quantity,
    }
    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'include_cart.html', {'carts': user_cart}, request=request
    )
    response_data = {
        'message': 'Product has been removed',
        "cart_items_html": cart_items_html,
        'quantity_deleted': quantity
    }
    return JsonResponse(response_data)
