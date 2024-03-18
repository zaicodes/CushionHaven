from django.shortcuts import render
from .models import Product
# Create your views here.
products = Product.objects.all()
contexts = {
    'products': products,
}


def allproducts(request):
    return render(request, "products/products.html", contexts)
