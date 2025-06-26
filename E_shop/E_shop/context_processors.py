from cart.cart import Cart

def cart_total_amount(request):
    cart = Cart(request)
    total = 0
    for key, value in request.session.get('cart', {}).items():
        total += int(value['price']) * int(value['quantity'])
    return {'cart_total_amount': total}