from django.apps import AppConfig

"""
Code borrowed from CI's Boutique Ado project, Admin, Signals & Forms Part 1.
"""


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
