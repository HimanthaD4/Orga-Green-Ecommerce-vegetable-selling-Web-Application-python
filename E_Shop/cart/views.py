from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .cart import Cart  
from store_app.models import Product 
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/login/")
def item_clear_modal(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("home")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/login/")
def cart_clear2(request):
    cart = Cart(request)
    cart.clear()
    return redirect("home")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')


def Check_out(request):
    amount_str = request.POST.get('amount')
    amount_float = float(amount_str)
    amount = int(amount_float)

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture" : "1"
    })

    order_id = payment['id']
    context = {
        'order_id': order_id,
        'payment': payment,
    }
    return render(request,'Cart/checkout.html',context)






def PLACE_ORDER(request):
    if request.method == 'POST':
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        cart = request.session.get('cart')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')

        context = {
            'order_id':order_id,
        }

        order = Order(user=user, firstname=firstname, lastname=lastname, country=country, address=address,
                      city=city, state=state, email=email, payment_id=order_id, amount = amount)

        order.postcode = postcode
        order.phone = phone

        order.save()

        request.session['order_details'] = {
            'name': firstname,
            'order_id': order_id,
            'payment_id': payment,
            'total_price': amount,
            'address': address,
            'phone': phone,
            'country': country,
            'city': city,
            'state': state,
            'postcode': postcode,
            'email': email,
            'products': [
                {
                    'name': cart_item['name'],
                    'quantity': cart_item['quantity'],
                    'price': cart_item['price'],  # Include product price in the details
                }
                for cart_item in cart.values()
            ],
        }

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']

            total = a * b

            item = OrderItem(
                user = user,
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total
            )
            item.save()

    return render(request, 'Cart/placeorder.html',context)



@csrf_exempt
def SUCCESS(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break

        user = Order.objects.filter(payment_id = order_id).first()
        user.paid = True
        user.save()
    return render(request,'Cart/thank-you.html')



@login_required(login_url="/login/")
def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)

    order = OrderItem.objects.filter(user = user)
    context = {
        'order':order,
    }

    return render(request,'Main/your_order.html',context)