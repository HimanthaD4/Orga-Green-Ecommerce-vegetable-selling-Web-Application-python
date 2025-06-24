from django import template
from django.conf import settings
from store_app.models import Product  # Adjust import based on your actual model location

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiply price by quantity"""
    try:
        return float(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.simple_tag(takes_context=True)
def cart_item_count(context):
    """Get total number of items in cart"""
    request = context['request']
    if hasattr(request, 'session'):
        cart = request.session.get(settings.CART_SESSION_ID, {})
        return sum(int(item['quantity']) for item in cart.values())
    return 0

@register.simple_tag(takes_context=True)
def cart_total_amount(context):
    """Calculate total cart amount"""
    request = context['request']
    total = 0
    if hasattr(request, 'session'):
        cart = request.session.get(settings.CART_SESSION_ID, {})
        for item in cart.values():
            total += float(item['price']) * int(item['quantity'])
    return total

@register.simple_tag(takes_context=True)
def product_in_cart(context, product_id):
    """Check if product exists in cart"""
    request = context['request']
    if hasattr(request, 'session'):
        cart = request.session.get(settings.CART_SESSION_ID, {})
        return str(product_id) in cart
    return False

@register.simple_tag(takes_context=True)
def get_cart_product(context, product_id):
    """Get cart product details"""
    request = context['request']
    if hasattr(request, 'session'):
        cart = request.session.get(settings.CART_SESSION_ID, {})
        return cart.get(str(product_id))
    return None