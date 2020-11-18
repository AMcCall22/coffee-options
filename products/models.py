from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Bean(models.Model):
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    bag_size = models.CharField(max_length=254)
    description = models.TextField()
    sizes = models.BooleanField(default=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    strength = models.CharField(max_length=5)
    image = models.ImageField()

    def __str__(self):
        return self.bag_size
