from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
Code borrowed from CI's Boutique Ado project, Admin, Signals & Forms Part 1. 
"""

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
