from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Product
from .models import Cart, CartItem, Order, OrderItem

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        cart_item.quantity = int(request.POST.get('quantity'))
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=cart.total_price)
        for cart_item in cart.cartitem_set.all():
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
        cart.cartitem_set.all().delete()  # Clear the cart after checkout
        return redirect('order_confirmation')
    return render(request, 'cart/checkout.html', {'cart': cart})

@login_required
def order_confirmation(request):
    order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    return render(request, 'cart/order_confirmation.html', {'order': order})

