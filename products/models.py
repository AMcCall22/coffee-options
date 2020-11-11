from django.db import models


class Bean(models.Model):
    country = models.CharField(max_length=254)
    description = models.TextField()
    sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    strength = models.CharField(max_length=5)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.country
