from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect

from user.models import User
from product.models import Product
# from .models import Wishlist

def wishlist_view(request):

    current_user = get_object_or_404(User, id=request.user.id)
    wishlist_objects = current_user.wishlist_items.all
    context ={
        'wishlist': wishlist_objects
    }
    return render(request, 'wishlist/wishlist_view.html', context)

def update_wishlist_view(request, my_id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    current_user = get_object_or_404(User, id=request.user.id)
    if my_id is not None:
        current_product = get_object_or_404(Product, id = my_id)
        if current_product in current_user.cart_items.all():
            current_user.cart_items.remove(current_product)
        if not current_product in current_user.wishlist_items.all():
            current_user.wishlist_items.add(current_product)
        else:
            current_user.wishlist_items.remove(current_product)

    return redirect(reverse ('product-detail', kwargs={ 'my_id':my_id}))