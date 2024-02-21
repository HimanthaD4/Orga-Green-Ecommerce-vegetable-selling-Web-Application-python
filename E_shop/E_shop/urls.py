from django.contrib import admin
from django.urls import path
from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls.static import static
from .import views

from .views import generate_pdf

app_name = 'cart'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.HOME,name='home'),
    path('main/',views.MAIN,name='main'),
    path('base/',views.BASE,name='base'),
    path('products/',views.PRODUCT,name='products'),
    path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name='product_detail'),
    path('search/',views.SEARCH,name='search'),
    path('contact/',views.Contact_Page,name='contact'),
    path('register/',views.HandleRegister,name='register'),
    path('login/',views.HandleLogin,name='login'),
    path('logout/',views.HandleLogout,name='logout'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_clear_modal/<int:id>/', views.item_clear_modal, name='item_clear_modal'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_clear2/', views.cart_clear2, name='cart_clear2'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',views.Check_out,name='checkout'),
    path('cart/checkout/placeorder',views.PLACE_ORDER,name='place_order'),
    path('success/',views.SUCCESS,name='success'),
    path('about/',views.ABOUT,name='about'),
    path('forgot/',views.FORGOT,name='forgot'),


    path('Your_Order/',views.Your_Order,name='your_order'),

    path('fertilizer/', views.FERTILIZER, name='fertilizer'),
    path('gap/', views.GAP, name='gap'),
    path('ph/', views.PH, name='ph'),
    path('crop/', views.CROP, name='crop'),

    path('green/', views.GREEN, name='green'),
    path('brinjal/', views.BRINJAL, name='brinjal'),
    path('tomato/', views.TOMATO, name='tomato'),
    path('papaw/', views.PAPAW, name='papaw'),
    path('mushroom/', views.MUSHROOM, name='mushroom'),

    path('forgot/', views.FORGOT, name='forgot'),
    path('update_password/', views.update_password, name='update_password'),

    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

