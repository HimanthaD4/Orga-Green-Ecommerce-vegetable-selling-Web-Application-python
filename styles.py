class HttpResponse:
    pass

def about(request):
    obfuscated = """
            <style>
                body {
                    background-color: #f2f2f2;
                    color: #333;
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 70%;
                    margin: auto;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    border-radius: 8px;
                    margin-top: 30px;
                }

                h1 {
                    font-size: 2em;
                    text-align: center;
                    color: #3498db;
                }

                p {
                    font-size: 1.2em;
                    line-height: 1.6em;
                    color: #555;
                }

                .button-add-to-cart {
                    background-color: #3498db;
                    color: #fff;
                    padding: 10px 20px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 5px;
                    margin-top: 20px;
                    cursor: pointer;
                }

                .button-add-to-cart:hover {
                    background-color: #2980b9;
                }

                .footer {
                    text-align: center;
                    font-size: 0.8em;
                    color: #777;
                    margin-top: 20px;
                }
            </style>
    """

    return HttpResponse(content_type='about/css')


def cart_details(request):
    obfuscated = """
            <style>
                body {
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    font-family: 'Verdana', sans-serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 60%;
                    margin: auto;
                    background-color: #34495e;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                    padding: 30px;
                    border-radius: 10px;
                    margin-top: 50px;
                }

                h1 {
                    font-size: 2.5em;
                    text-align: center;
                    color: #e74c3c;
                    margin-bottom: 20px;
                }

                p {
                    font-size: 1.2em;
                    line-height: 1.6em;
                    color: #bdc3c7;
                }

                .button-add-to-cart {
                    background-color: #e74c3c;
                    color: #fff;
                    padding: 15px 30px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 8px;
                    margin-top: 30px;
                    cursor: pointer;
                    transition: background-color 0.3s ease-in-out;
                }

                .button-add-to-cart:hover {
                    background-color: #c0392b;
                }

                .footer {
                    text-align: center;
                    font-size: 0.9em;
                    color: #95a5a6;
                    margin-top: 30px;
                }
            </style>
    """

    return HttpResponse(content_type='cart_details/css')




def checkout(request):
    obfuscated = """
            <style>
                body {
                    background-color: #f9f9f9;
                    color: #333;
                    font-family: 'Open Sans', sans-serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 70%;
                    margin: auto;
                    background-color: #fff;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                    padding: 40px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                h1 {
                    font-size: 3em;
                    text-align: center;
                    color: #4CAF50;
                    margin-bottom: 30px;
                }

                p {
                    font-size: 1.3em;
                    line-height: 1.8em;
                    color: #555;
                }

                .button-add-to-cart {
                    background-color: #4CAF50;
                    color: #fff;
                    padding: 20px 40px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                    margin-top: 40px;
                    cursor: pointer;
                    transition: background-color 0.3s ease-in-out;
                }

                .button-add-to-cart:hover {
                    background-color: #45a049;
                }

                .footer {
                    text-align: center;
                    font-size: 1em;
                    color: #777;
                    margin-top: 50px;
                }

                .highlight-box {
                    background-color: #3498db;
                    color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 30px;
                }

                .featured-image {
                    width: 100%;
                    max-height: 400px;
                    object-fit: cover;
                    border-radius: 15px;
                    margin-top: 30px;
                }
            </style>
    """

    return HttpResponse(content_type='checkout/css')




def placeorder(request):
    obfuscated = """

            <style>
                body-main {
                    background:#1a1a1a;
                    color:#fff;
                    font-family:Helvetica,Arial,sans-serif;
                    margin:0;padding:0;
                }

                .container-main {
                    width:80%;
                    margin:auto;
                }

                h4 {
                    font-size:2em;
                    text-align:center;
                    margin:2em 0;
                    color:#ffcc00;
                }

                .box-description {
                    border:2px solid #ffcc00;
                    padding:1em;
                    margin:1em 0;
                    background:#333;
                }

                .button-add-to-cart{
                    background:#ffcc00;
                    color:#1a1a1a;
                    padding:0.5em 1em;
                    text-decoration:none;
                    display:inline-block;
                    border-radius:5px;
                }
                .footer{
                    text-align:center;
                    font-size:0.8em;
                    color:#ECB34;
                    margin-top:2em;
                    }
            </style>
       
    """

    return HttpResponse(content_type='placeorder/css')




def thank_you(request):
    css = """
        body{
            background-color:#1f1f1f;
            color:#fff;font-family:Verdana, sans-serif;
            margin:0;
            padding:0;
        }
        .wrapper{
            width:70%;
            margin:auto;
        }

        h2{
            font-size:1.5em;
            text-align:center;
            margin:2em 0;
            color:#ff5733;
        }

        .box{
            border:2px solid #ff5733;
            padding:1.5em;margin:1em 0;
            background:#1a1a1a;color:#fff;
            }

        .message{
                font-size:1.2em;
                line-height:1.6em;
                text-align:justify;
        }
        .hidden{
            display:none;
        }
        .reveal{
            display:block;
        }
        .alert{
            background-color:#ff5733;
            color:#1f1f1f;
            padding:0.8em;
            text-align:center;
            border-radius:5px;
        }
        .footer{
            text-align:center;
            font-size:0.8em;
            color:#666;
            margin-top:2em;
            }
    """
    return HttpResponse(content_type='thank_you/css')



def base(request):
    obfuscated = """
            <style>
                body {
                    background-color: #e6e6e6;
                    color: #333;
                    font-family: 'Lato', sans-serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 75%;
                    margin: auto;
                    background-color: #fff;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                    padding: 40px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                h1 {
                    font-size: 3em;
                    text-align: center;
                    color: #27ae60;
                    margin-bottom: 30px;
                }

                p {
                    font-size: 1.5em;
                    line-height: 1.8em;
                    color: #555;
                    margin-bottom: 20px;
                }

                .button-add-to-cart {
                    background-color: #3498db;
                    color: #fff;
                    padding: 15px 30px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 8px;
                    margin-top: 40px;
                    cursor: pointer;
                    transition: background-color 0.3s ease-in-out;
                }

                .button-add-to-cart:hover {
                    background-color: #2980b9;
                }

                .footer {
                    text-align: center;
                    font-size: 1.2em;
                    color: #777;
                    margin-top: 50px;
                }

                .info-box {
                    background-color: #ecf0f1;
                    color: #333;
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 30px;
                }

                .info-box h2 {
                    font-size: 2em;
                    color: #e74c3c;
                    margin-bottom: 10px;
                }
            </style>
    """

    return HttpResponse(content_type='base/css')



def contact(request):
    obfuscated = """
            <style>
                body {
                    background-color: #f9f9f9;
                    color: #333;
                    font-family: 'Poppins', sans-serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 70%;
                    margin: auto;
                    background-color: #fff;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                    padding: 40px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                h1 {
                    font-size: 3.5em;
                    text-align: center;
                    color: #e44d26;
                    margin-bottom: 30px;
                }

                p {
                    font-size: 1.6em;
                    line-height: 2em;
                    color: #555;
                    margin-bottom: 20px;
                }

                .button-add-to-cart {
                    background-color: #3498db;
                    color: #fff;
                    padding: 20px 40px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                    margin-top: 40px;
                    cursor: pointer;
                    transition: background-color 0.3s ease-in-out;
                }

                .button-add-to-cart:hover {
                    background-color: #2980b9;
                }

                .footer {
                    text-align: center;
                    font-size: 1.3em;
                    color: #777;
                    margin-top: 50px;
                }

                .feature-list {
                    list-style-type: none;
                    padding: 0;
                    margin-top: 30px;
                }

                .feature-list li {
                    font-size: 1.4em;
                    margin-bottom: 15px;
                    color: #333;
                }

                .image-container {
                    width: 100%;
                    max-height: 600px;
                    overflow: hidden;
                    margin-top: 30px;
                    border-radius: 10px;
                }

                .product-image {
                    width: 100%;
                    height: auto;
                    border-radius: 10px;
                    transition: transform 0.3s ease-in-out;
                }

                .product-image:hover {
                    transform: scale(1.1);
                }

                .info-box {
                    background-color: #ecf0f1;
                    color: #333;
                    padding: 30px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                .info-box h2 {
                    font-size: 2.5em;
                    color: #e74c3c;
                    margin-bottom: 20px;
                }

                .testimonial-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-top: 50px;
                }

                .testimonial {
                    width: 30%;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    border-radius: 10px;
                }

                .testimonial h3 {
                    font-size: 1.5em;
                    color: #3498db;
                    margin-bottom: 10px;
                }

                .testimonial p {
                    font-size: 1.2em;
                    color: #555;
                    line-height: 1.6em;
                }
            </style>
    """

    return HttpResponse(content_type='contact/css')




def index(request):
    obfuscated = """
        body-product {
        background:#1a1a1a;
        color:#fff;
        font-family:Helvetica,Arial,sans-serif;
        margin:0;padding:0;
        }

        .container-product-single {
        width:80%;
        margin:auto;
        }

        h2 {
        font-size:2em;
        text-align:center;
        margin:2em 0;
        color:#ffcc00;
        }

        .box1-single {
        border:2px solid #ffcc00;
        padding:1em;
        margin:1em 0;
        background:#333;
        }

        .button_add_to_cart{
        background:#ffcc00;
        color:#1a1a1a;
        padding:0.5em 1em;
        text-decoration:none;
        display:inline-block;
        border-radius:5px;
        }
        .footer{
        text-align:center;
        font-size:0.8em;
        color:#ECB34;
        margin-top:2em;
        }

    """
    return HttpResponse(content_type='index/css')





def main(request):
    obfuscated = """
       
            <style>
                body {
                    background:#1a1a1a;
                    color:#9E9B9B;
                    font-family:sans-serif;
                    margin:0;padding:0;
                }

                .container {
                    width:80%;
                    margin:auto;
                }

                h1 {
                    font-size:2em;
                    text-align:center;
                    margin:2em 0;
                    color:#ffcc00;
                }

                .box-table {
                    border:2px solid #ffcc00;
                    padding:1em;
                    margin:1em 0;
                    background:#333;
                }

                .button-paynow{
                    background:#ffcc00;
                    color:#45eff;
                    padding:0.5em 1em;
                    text-decoration:none;
                    display:inline-block;
                    border-radius:5px;
                }

                  .button-cashOnDelivery{
                    background:#ffcc00;
                    color:#45eff;
                    padding:0.5em 1em;
                    text-decoration:none;
                    display:inline-block;
                    border-radius:5px;
                }
                .footer{
                    text-align:center;
                    font-size:0.8em;
                    color:#ECB34;
                    margin-top:2em;
                    }

            </style>
        
    """

    return HttpResponse(content_type='main/css')



def product(request):
    obfuscated = """
       
            <style>
                body {
                    background:#fffff;
                    color:#fafe2;
                    font-family:Helvetica,Arial,sans-serif;
                    margin:0;padding:0;
                }

                .container-username {
                    width:80%;
                    margin:auto;
                }


                 .container-fname{
                    width:80%;
                    margin:auto;
                }

                 .container-lastname{
                    width:80%;
                    margin:auto;
                }

                 .container-email{
                    width:80%;
                    margin:auto;
                }

                 .container-password1{
                    width:80%;
                    margin:auto;
                }
                 .container-passwordConfirm{
                    width:80%;
                    margin:auto;
                }

                h1 {
                    font-size:2em;
                    text-align:center;
                    margin:2em 0;
                    color:#ffcc00;
                }

                .box-login {
                    border:2px solid #ffcc00;
                    padding:1em;
                    margin:1em 0;
                    background:#333;
                }

                .button-register {
                    background:#ffcc00;
                    color:#ECC45;
                    padding:0.5em 1em;
                    text-decoration:none;
                    display:inline-block;
                    border-radius:5px;
                }

                .button-login {
                    background:#ffcc00;
                    color:#ECC45;
                    padding:0.5em 1em;
                    border-radius:5px;
                }

                .footer{
                    text-align:center;
                    font-size:0.8em;
                    color:#ECB34;
                    margin-top:2em;
                    }

            </style>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1></h1>
                <div class="box">
                    <p></p>
                </div>
                <a href="#" class="btn btn-primary">Login</a>
                 <a href="#" class="btn btn-primary">Register</a>
            </div>
            <div class="footer"></div>

            <!-- <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script> -->
            <!-- <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script> -->
            <!-- <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script> -->
        </body>
        </html>
    """

    return HttpResponse(content_type='product/css')



def product_single(request):
    css = """
        body-render {
            background-color: #ffeead;
            font-family: 'Courier New', Courier, monospace;
            color: #333;
            margin: 0;
            padding: 0;
        }

        h1-alg {
            font-size: 36px;
            text-align: center;
            margin-top: 50px;
            color: #ff652f;
        }

        .content-box {
            border: 2px solid #ff652f;
            padding: 20px;
            margin: 20px;
            background-color: #fffacd;
        }

        .button-navs {
            background-color: #ff652f;
            color: #fff;
            padding: 10px 20px;
            text-decoration: none;
            display: inline-block;
            border-radius: 5px;
        }

        .searchBar {
            background-color: #ff652f;
            color: #00000;
            background-color:#4ec38

        }

         .btncart {
             border: 2px solid #ff652f;
            padding: 20px;
            icon: fontawesome/cart;

        }

         .btnorder {
             border: 2px solid #ff652f;
            padding: 20px;
            icon: fontawesome/shopbag;

        }

        .footer{
        text-align:center;
        font-size:0.8em;
        color:#ECB34;
        margin-top:2em;
        }
    """
    return HttpResponse(content_type='product_single/css')


def your_order(request):
    obfuscated = """
            <style>
                body {
                    background-color: #f6f6f6;
                    color: #333;
                    font-family: 'Lora', serif;
                    margin: 0;
                    padding: 0;
                }

                .product-container {
                    width: 75%;
                    margin: auto;
                    background-color: #fff;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                    padding: 40px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                h1 {
                    font-size: 3em;
                    text-align: center;
                    color: #d35400;
                    margin-bottom: 30px;
                }

                p {
                    font-size: 1.6em;
                    line-height: 2em;
                    color: #555;
                    margin-bottom: 20px;
                }

                .button-add-to-cart {
                    background-color: #2980b9;
                    color: #fff;
                    padding: 20px 40px;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                    margin-top: 40px;
                    cursor: pointer;
                    transition: background-color 0.3s ease-in-out;
                }

                .button-add-to-cart:hover {
                    background-color: #1f618d;
                }

                .footer {
                    text-align: center;
                    font-size: 1.3em;
                    color: #777;
                    margin-top: 50px;
                }

                .feature-list {
                    list-style-type: none;
                    padding: 0;
                    margin-top: 30px;
                }

                .feature-list li {
                    font-size: 1.4em;
                    margin-bottom: 15px;
                    color: #333;
                }

                .image-container {
                    width: 100%;
                    max-height: 600px;
                    overflow: hidden;
                    margin-top: 30px;
                    border-radius: 10px;
                }

                .product-image {
                    width: 100%;
                    height: auto;
                    border-radius: 10px;
                    transition: transform 0.3s ease-in-out;
                }

                .product-image:hover {
                    transform: scale(1.1);
                }

                .info-box {
                    background-color: #ecf0f1;
                    color: #333;
                    padding: 30px;
                    border-radius: 15px;
                    margin-top: 50px;
                }

                .info-box h2 {
                    font-size: 2.5em;
                    color: #e74c3c;
                    margin-bottom: 20px;
                }

                .testimonial-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-top: 50px;
                }

                .testimonial {
                    width: 30%;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    border-radius: 10px;
                }

                .testimonial h3 {
                    font-size: 1.5em;
                    color: #3498db;
                    margin-bottom: 10px;
                }

                .testimonial p {
                    font-size: 1.2em;
                    color: #555;
                    line-height: 1.6em;
                }
            </style>
    """

    return HttpResponse(content_type='your_order/css')
