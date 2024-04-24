from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success, name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'),
    path(
        'edit_address/<int:address_id>/',
        views.edit_address, name='edit_address'),
    path(
        'delete_address/<int:pk>/',
        views.AddressDeleteView.as_view(), name='delete_address'),
    path('wh/', webhook, name='webhook'),

]
