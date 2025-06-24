from cart.cart import Cart

def cart_total_amount(request):
    cart = Cart(request)
    total = cart.get_total_price()
    return {'cart_total_amount': total}