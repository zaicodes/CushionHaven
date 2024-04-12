from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    # A view that renders the bag contents page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # Add a quantity of the specified product to the shopping bag

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag and size in bag[item_id]['items_by_size']:
            bag[item_id]['items_by_size'][size] += quantity
            message = (
                'Updated size ' + size.upper() + ' ' + product.name +
                ' quantity to ' + str(bag[item_id]["items_by_size"][size])
            )
            messages.success(request, message)
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, message)
    else:
        if item_id in bag:
            bag[item_id] += quantity
            message = 'Update ' + product.name + 'quantity' + str(bag[item_id])
            messages.success(request, message)
        else:
            bag[item_id] = quantity
            message = 'Added ' + product.name + ' to your bag'
            messages.success(request, message)

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    # Adjust the quantity of the specified product to the specified amount

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            message = (
                'Updated size ' + size.upper() + ' ' + product.name +
                ' quantity to ' + str(bag[item_id]["items_by_size"][size])
            )
            messages.success(request, message)
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            message = 'Removed size ' + size.upper() + ' ' + product.name
            messages.success(request, message)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            message = 'Update ' + product.name + 'quantity' + str(bag[item_id])
            messages.success(request, message)
        else:
            bag.pop(item_id)
            message = 'Removed ' + product.name + ' from your bag'
            messages.success(request, message)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    # Remove the item from the shopping bag

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size', None)
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            message = f'{size.upper()} {product.name} from your bag'
            messages.success(request, message)
        else:
            bag.pop(item_id)
            message = 'Removed ' + product.name + ' from your bag'
            messages.success(request, message)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        message = 'Error removing item: ' + str(e)
        messages.error(request, message)
