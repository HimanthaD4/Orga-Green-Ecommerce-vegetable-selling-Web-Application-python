from io import BytesIO
from django.shortcuts import render,redirect
from pyexpat.errors import messages
from store_app.models import Product,Categories,Contact_us,Order,OrderItem
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
import razorpay
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib import messages

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))

def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status = 'Publish')
    context = {
        'product': product,
    }
    return render(request,'Main/index.html',context)


def MAIN(request):
    product = Product.objects.filter(status = 'Publish')
    context = {
        'product': product,
    }
    return render(request,'Main/main.html',context)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    # filter_price = Filter_price.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories = CATID)
    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories':categories,
        # 'filter_price':filter_price,
    }
    return render(request,'Main/product.html',context)



def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product': product
    }
    return render(request, 'Main/search.html',context)


def PRODUCT_DETAIL_PAGE(request,id):
    prod = Product.objects.filter(id = id).first()
    context = {
        'prod': prod
    }
    return render (request,'Main/product_single.html',context)


def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return redirect('home')
    return render(request,'Main/contact.html')


def HandleRegister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        try:
            existing_user = User.objects.get(username=username)
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('register')
        except User.DoesNotExist:
            pass

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match. Please enter matching passwords.')
            return redirect('register')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'Registration/auth.html')



def HandleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            try:
                user = User.objects.get(username=username)
                messages.error(request, 'Username and password do not match. Please try again.')
            except User.DoesNotExist:
                messages.error(request, 'Username does not exist. Please register before logging in.')
            return redirect('login')

    return render(request, 'Registration/auth.html')


def HandleLogout(request):
    logout(request)
    return redirect('home')

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
    amount = int(amount_float*100)

    payment = client.order.create({
        "amount": amount,
        "currency": "LKR",
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
                    'price': cart_item['price'],  
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

def ABOUT(request):
    return render(request, 'Cart/about.html')

def FORGOT(request):
    return render(request, 'Registration/forgotPassword.html')

def FERTILIZER(request):
    return render(request,'Catalog/fertilizer.html')

def GAP(request):
    return render(request,'Catalog/gapIntro.html')

def PH(request):
    return render(request,'Catalog/phMesure.html')

def CROP(request):
    return render(request,'Catalog/cropDisease.html')

def GREEN(request):
    return render(request,'Catalog/greenChilli.html')

def BRINJAL(request):
    return render(request,'Catalog/brinjal.html')

def TOMATO(request):
    return render(request,'Catalog/tomato.html')

def PAPAW(request):
    return render(request,'Catalog/papaw.html')

def MUSHROOM(request):
    return render(request,'Catalog/mushroom.html')

def update_password(request):
    user = None

    if request.method == 'POST':
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
            return render(request, 'Registration/forgotPassword.html')

        if not user.check_password(old_password):
            messages.error(request, 'Invalid old password.')
        elif new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
        else:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully.')
            return render(request, 'Registration/forgotPassword.html')

    messages_in_context = messages.get_messages(request)
    return render(request, 'Registration/forgotPassword.html', {'messages': messages_in_context, 'user': user})


def generate_pdf(request):
    styles = getSampleStyleSheet()

    order_details = request.session.get('order_details', {})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="order_details.pdf"'

    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)

    elements = []

    brand_name = "healthyGoods"
    slogan = "Fresh. Healthy. Delivered with care."
    brand_header_style = ParagraphStyle('BrandHeader', parent=styles['Title'], fontSize=18, textColor=colors.green)
    brand_paragraph = Paragraph(f"<b>{brand_name}</b><br/>{slogan}", brand_header_style)
    elements.append(brand_paragraph)

    company_paragraph = (
        "At HealthyGoods, we are committed to providing you with the freshest and highest quality fruits and vegetables. "
        "Our mission is to promote a healthy lifestyle by delivering farm-fresh produce directly to your doorstep. "
        "With a focus on quality and customer satisfaction, we take pride in offering a wide range of organic and "
        "locally sourced products. Thank you for choosing healthyGoods for your healthy living journey."
    )
    elements.append(Paragraph(company_paragraph, styles['Normal']))

    order_id = order_details.get('order_id', '')
    if order_id:
        elements.append(Paragraph(f"Order ID: {order_id}", styles['Heading2']))

    elements.append(Paragraph("Order Details", styles['Title']))

    elements.append(Paragraph("Customer Information:", styles['Heading2']))
    customer_info = [
        f"Name: {order_details['name']}",
        f"Email: {order_details['email']}",
        f"Phone: {order_details['phone']}"
    ]
    elements.extend([Paragraph(info, styles['Normal']) for info in customer_info])

    elements.append(Spacer(1, 12))  # Add space

    elements.append(Paragraph("Address Details:", styles['Heading2']))
    address_info = [
        f"Address: {order_details['address']}",
        f"City: {order_details['city']}",
        f"State: {order_details['state']}",
        f"Postcode: {order_details['postcode']}"
    ]
    elements.extend([Paragraph(info, styles['Normal']) for info in address_info])

    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Product Details:", styles['Heading2']))
    product_details = order_details.get('products', [])
    table_data = [['Product', 'Quantity', 'Price', 'Total Price']]
    for product in product_details:
        quantity = product['quantity']
        price = float(product['price'])
        total_price = quantity * price
        table_data.append([product['name'], str(quantity), f'Rs. {price}', f'Rs. {total_price}'])

    col_widths = [doc.width / 4] * 4
    table = Table(table_data, colWidths=col_widths)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Add borders
    ]))

    elements.append(table)

    elements.append(Spacer(1, 12))

    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    elements.append(Paragraph(f"Date: {current_date}", styles['Normal']))
    elements.append(Paragraph(f"Time: {current_time}", styles['Normal']))

    elements.append(Spacer(1, 12))

    total_amount = f"Total Amount: Rs. {order_details.get('total_price', 0)}"
    elements.append(Paragraph(total_amount, styles['Heading2']))

    return_policy = "Not allowed to return orders within 3 days after delivery."
    elements.append(Paragraph(return_policy, styles['Normal']))

    doc.build(elements)

    pdf_value = pdf_buffer.getvalue()
    pdf_buffer.close()
    response.write(pdf_value)

    return response


