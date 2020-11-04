from django.db import models


class Coffee(models.Model):
    country = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    strength = models.CharField(max_length=5)
    image = models.ImageField()

    def __str__(self):
        return self.country
