import uuid

from django.db import models
from django.db.models import Sum

from products.models import Bean
from profiles.models import UserProfile

from django_countries.fields import CountryField

"""
Code adapted from from CI's Boutique Ado project, Checkout section
"""


class Order(models.Model):
    """
    A model for each order in the database.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
                                      

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added

        """
        print("updating total")
        sys.stdout.flush() 
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=True, related_name='lineitems')
    bean = models.ForeignKey(Bean, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        print("OLI save")
        sys.stdout.flush()
        self.lineitem_total = self.bean.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return '{self.bean.country} on order {self.order.order_number}'
