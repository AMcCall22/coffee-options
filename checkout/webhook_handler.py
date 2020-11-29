from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Bean
from profiles.models import UserProfile
import sys

import json
import time

"""
Code adapted from from CI's Boutique Ado project, Checkout section
"""


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        print("send email")
        sys.stdout.flush() 
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print("pay intent succeeded")
        sys.stdout.flush()
        intent = event.data.object
        pid = intent.id
        shopping_bag = intent.metadata.shopping_bag
        save_info = intent.metadata.shopping_bag
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        print("updating profile")
        sys.stdout.flush() 
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.default_phone_number = shipping_details.phone
                profile.save()
        print("running attempts")
        sys.stdout.flush() 
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                print("att", attempt)
                sys.stdout.flush()
                try:
                    order = Order.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        town_or_city__iexact=shipping_details.address.city,
                        postcode__iexact=shipping_details.address.postal_code,
                        country__iexact=shipping_details.address.country,
                        phone_number__iexact=shipping_details.phone,
                        order_total=order_total,
                        stripe_pid=pid,
                    )
                except:
                    print(sys.exc_info()[0])
                    sys.stdout.flush()
                print("order found")
                sys.stdout.flush()
                order_exists = True
                print("breaking")
                sys.stdout.flush()
                break
            except Order.DoesNotExist:
                print("except")
                sys.stdout.flush()
                attempt += 1
                time.sleep(1)
            print("broke")
            sys.stdout.flush()
        if order_exists:
            print("order exists")
            sys.stdout.flush()
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            print("else order not exist")
            sys.stdout.flush() 
            order = None
            try:
                print("trying")
                sys.stdout.flush() 
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    email=billing_details.email,
                    town_or_city=shipping_details.address.city,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    phone_number=shipping_details.phone,
                )
                for item_id, item_data in json.loads(shopping_bag).items():
                    bean = Bean.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            bean=bean,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=bean,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                print("error", e)
                sys.stdout.flush() 
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        print("sending email")
        sys.stdout.flush()
        self._send_confirmation_email(order)
        print("return 200")
        sys.stdout.flush() 
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print("intent failed")
        sys.stdout.flush()
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
