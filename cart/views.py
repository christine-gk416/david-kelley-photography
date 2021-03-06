from django.shortcuts import(render, redirect, reverse,
                             HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    cart = request.session.get('cart', {})

    if color:
        if item_id in list(cart.keys()):
            if color in cart[item_id]['items_by_color'].keys():
                cart[item_id]['items_by_color'][color] += quantity
                messages.success(request, f'Updated color {color.upper()} \
                                 {product.name} quantity to \
                                 {cart[item_id]["items_by_color"][color]}')
            else:
                cart[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Added color \
                                 {color.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'Added color \
                             {color.upper()} {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} \
                             quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
        cart = request.session.get('cart', {})

    if color:
        if quantity > 0:
            cart[item_id]['items_by_color'][color] = quantity
            messages.success(request, f'Updated color {color.upper()} \
                             {product.name} quantity to \
                             {cart[item_id]["items_by_color"][color]}')
        else:
            del cart[item_id]['items_by_color'][color]
            if not cart[item_id]['items_by_color']:
                cart.pop(item_id)
            messages.success(request, f'Removed color {color.upper()} \
                             {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} \
                             quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        cart = request.session.get('cart', {})

        if color:
            del cart[item_id]['items_by_color'][color]
            if not cart[item_id]['items_by_color']:
                cart.pop(item_id)
            messages.success(request, f'Removed color {color.upper()} \
                             {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
