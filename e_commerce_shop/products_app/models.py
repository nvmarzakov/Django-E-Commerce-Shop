# products_app models.py
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    # return a queryset with filter
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    MAX_LENGTH_CATEGORY = 255

    name = models.CharField(
        max_length=MAX_LENGTH_CATEGORY,
        db_index=True,
    )

    slug = models.SlugField(
        max_length=MAX_LENGTH_CATEGORY,
        unique=True,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products_app:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    MAX_PRODUCT_LENGTH = 255
    MAX_BRAND_LENGTH = 30

    category = models.ForeignKey(
        Category,
        related_name='product',
        on_delete=models.CASCADE,
    )
    # shows who create the products
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product_creator'
    )

    title = models.CharField(
        max_length=MAX_PRODUCT_LENGTH,
    )

    brand = models.CharField(
        max_length=MAX_BRAND_LENGTH,
    )

    description = models.TextField(
        blank=True,
    )

    weight = models.PositiveIntegerField(
        null=True,
    )

    image = models.ImageField(
        upload_to='images/',
        # if forget to upload image, will show default.png
        default='images/default.png',
    )

    slug = models.SlugField(
        max_length=MAX_PRODUCT_LENGTH,
    )

    # stock ot not
    in_stock = models.BooleanField(
        default=True,
    )

    # if out of stock
    is_active = models.BooleanField(
        default=True,
    )

    # To track the available quantity
    quantity = models.PositiveIntegerField(
        default=0,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('products_app:product_detail', args=[self.pk])

    def __str__(self):
        return self.title
