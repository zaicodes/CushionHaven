from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
    path('checkout/edit_address/<int:address_id>/',
         views.edit_address, name='edit_address'),
    path('wh/', webhook, name='webhook'),
    path('delete_address/<int:address_id>/',
         views.delete_address, name='delete_address'),
]
