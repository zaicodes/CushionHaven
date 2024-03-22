# from django.shortcuts import render  , get_object_or_404
# from .models import Product


# # Create your views here.
# def allproducts(request):
#     products = Product.objects.all()
#     contexts = {
#     'products': products,
#     }


#     return render(request, "products/products.html", contexts)
# # Create products details.
# def product_detail(request , product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     contexts = {
#     'products': product,
#     }


#     return render(request, "products/product_detail.html", contexts)
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_detail.html', context)