from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Category model"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('Category', related_name='products',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    has_colors = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            related_name="user_wishlist",
                                            blank=True)

    def __str__(self):
        return self.name
