"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from product.views import (
    product_view,
    product_create_view,
    dynamic_lookup_view,
    search,
    contact_view,
)

from user.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

from wishlist.views import(
    wishlist_view,
    update_wishlist_view,
)

from cart.views import(
    cart_view,
    update_cart_view,
    order_summary_view,
    delete_item_from_ordersummary,
    checkout_view,
    myorders_view,
    delete_from_order_view,
)


urlpatterns = [

    path('admin/', admin.site.urls),

    # product views
    path('', product_view, name = 'productscreen'),
    path('create/', product_create_view, name = 'product-create'),
    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('results/s', search, name = 'search'),

    path('contact/', contact_view, name='contact'),

    

    #wishlist views
    path('wishlist/', wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:my_id>/', update_wishlist_view, name='update_wishlist'),
    

    #cart views
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:my_id>/', update_cart_view, name="update_cart"),
    path('deleteitem/<int:my_id>/', delete_item_from_ordersummary, name='delete-item-from-ordersummary'),
    path('order-summary/', order_summary_view, name='order-summary'),
    path('checkout/', checkout_view, name='checkout'),
    path('myorders/', myorders_view, name='myorders'),
    path ('deleteorderitem/<int:my_id>/', delete_from_order_view, name='delete-purchase-record'),

    #user views
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('myaccount/', account_view, name='myaccount'),
    


    #social account log in
    path('accounts/', include('allauth.urls')),
    
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

