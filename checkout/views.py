from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HZvULA0iUnJxd6qucotRs5YaPNorXx73IXRSLBJE8IuzZM6dkY1RnRoqaU1U6vdyESeQyvNuxA6xPTC6oUeKj5400XukCuYsd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
