from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect

from user.models import User
from product.models import Product
# from .models import Wishlist

def cart_view(request):

    current_user = get_object_or_404(User, id=request.user.id)
    cart_objects = current_user.cart_items.all
    context ={
        'cart': cart_objects
    }
    return render(request, 'cart/cart_view.html', context)

def update_cart_view(request, my_id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    current_user = get_object_or_404(User, id=request.user.id)
    if my_id is not None:
        current_product = get_object_or_404(Product, id = my_id)
        if current_product in current_user.wishlist_items.all():
            current_user.wishlist_items.remove(current_product)
        if not current_product in current_user.cart_items.all():
            current_user.cart_items.add(current_product)
        else:
            current_user.cart_items.remove(current_product)
    return redirect(reverse ('product-detail', kwargs={ 'my_id':my_id}))

def order_summary_view(request):
    current_user = get_object_or_404(User, id=request.user.id)
    ordered_objects = current_user.cart_items.all

    sum=0
    for item in current_user.cart_items.all():
        sum=sum + item.price    
    context ={
        'object': ordered_objects,
        'sum'   : sum
    }
    return render (request, 'cart/order_summary.html', context)

def delete_item_from_ordersummary(request, my_id):
    current_user = get_object_or_404(User, id=request.user.id)
    if my_id is not None:
        delete_product = get_object_or_404(Product, id = my_id)
        if delete_product in current_user.cart_items.all():
            current_user.cart_items.remove(delete_product)
    return redirect(reverse('order-summary'))

def checkout_view(request):

    current_user = get_object_or_404(User, id=request.user.id)
    for item in current_user.cart_items.all():
        current_user.ordered_items.add(item)
        current_user.cart_items.remove(item)
    context={
        'success':'Order/s placed successfully'
    }
    return render (request, 'cart/checkout.html', context)

def myorders_view(request):
    current_user = get_object_or_404(User, id=request.user.id)
    ordered_objects = current_user.ordered_items.all
    
    context ={
        'order': ordered_objects
    }
    return render(request, 'cart/myorders_view.html', context)

def delete_from_order_view(request, my_id):
    current_user = get_object_or_404(User, id=request.user.id)
    if my_id is not None:
        delete_order = get_object_or_404(Product, id = my_id)
        if delete_order in current_user.ordered_items.all():
            current_user.ordered_items.remove(delete_order)
    return redirect(reverse('myorders'))

