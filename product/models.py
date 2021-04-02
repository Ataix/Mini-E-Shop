from time import time

from django.db import models
from django.urls import reverse

from pytils.translit import slugify


def gen_slug(s):
    slug = slugify(s)
    return slug


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, primary_key=True, blank=True)
    parent = models.ForeignKey('self',
                               related_name='children',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    short_title = models.SlugField(max_length=100, primary_key=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/img', default='/products/img/default_img.jpg', blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'short_title': self.short_title})

    def save(self, *args, **kwargs):
        if not self.short_title:
            self.short_title = gen_slug(self.title[:15]) + '-' + str(int(time()))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('price',)
